from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from enum import Enum
from threading import Timer
from threading import Lock
import time
import math
class IntegraLED:
    
    class LEDState(Enum):
        on = 0
        off = 1
        FadeIn = 2
        FadeOut = 3
        Unknown = 4
            
    def __init__(self, channel, levels=1000, linear=False):
        self.factory = PiGPIOFactory()
        self.led = PWMLED(channel, pin_factory=self.factory)
        self.led.off()
        self.led.frequency = 150
        self.state = self.LEDState.off
        self.levels = levels
        self.interval = 1.0/levels
        self.level = 0.0
        self.lock = Lock()
        self.linear = linear


    def doFadeIn(self, duration=5):
        self.setStateInterval(self.LEDState.FadeIn, duration)
    def doFadeOut(self, duration=5):
        self.setStateInterval(self.LEDState.FadeOut, duration)
    def doOn(self):
        self.setStateInterval(self.LEDState.on, 0)
    def doOff(self):
        self.setStateInterval(self.LEDState.off, 0)

    def doImmediateSwitch(self, state):
        if state:
            self.doOn()
        else:
            self.doOff()
        
    def doFade(self, state, duration=5):
        if state:
            self.doFadeIn(duration)
        else:
            self.doFadeOut(duration)
    
    def setStateInterval(self, state, duration):
        self.lock.acquire()
        try:
            self.t.cancel()
        except:
            pass
        self.state = state
        if duration != 0:
            self.interval = float(duration)/self.levels
        self.lock.release()
        self.updateDaemon()

    def updateDaemon(self):
        self.lock.acquire()
        # Do the fading if in that state
        if self.state == self.LEDState.FadeIn:
            self.level = self.level + 1.0/self.levels
        elif self.state == self.LEDState.FadeOut:
            self.level = self.level - 1.0/self.levels
        elif self.state == self.LEDState.on:
            self.level = 1.0
        elif self.state == self.LEDState.off:
            self.level = 0.0
        
        # Stop fade if level reached
        if self.level >= 1:
            self.level = 1
            self.state = self.LEDState.on
        elif self.level <= 0:
            self.level = 0
            self.state = self.LEDState.off

        if self.linear:
            self.led.value = self.level    
        else:
            k = 1.5
            #newValue = (math.exp(self.level*k) - 1)/(math.e**k - 1)
            newValue = float(self.level)**2
            newValue = 1 if newValue > 1 else newValue
            newValue = 0 if newValue < 0 else newValue
            
            self.led.value = newValue

        if (self.state == self.LEDState.FadeIn) | (self.state == self.LEDState.FadeOut):
            self.t = Timer(self.interval, self.updateDaemon)
            self.t.daemon = True
            self.t.start()
        self.lock.release()


if __name__ == "__main__":
    iled = IntegraLED("GPIO17")
    while True:
        iled.doOn()
        time.sleep(0.8)
        iled.doOff()
        time.sleep(0.8)
        iled.linear = False
        iled.doFadeIn(10)
        time.sleep(11)
        iled.doFadeOut(10)
        time.sleep(11)
        iled.linear = True
        iled.doFadeIn(10)
        time.sleep(11)
        iled.doFadeOut(10)
        time.sleep(11)