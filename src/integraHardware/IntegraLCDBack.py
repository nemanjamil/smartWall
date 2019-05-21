import rpi_backlight as bl
from enum import Enum
import time

class IntegraLCDBack:
    
    class LEDState(Enum):
        on = 0
        off = 1
        FadeIn = 2
        FadeOut = 3
        Unknown = 4
    
    def __init__(self, offLvl=64):
        bl.set_brightness(offLvl)
        self.state = self.LEDState.off
        self.level = offLvl
        self.offLvl = offLvl
    def doFadeIn(self, duration=5):
        bl.set_brightness(255, smooth=True, duration=duration)
    def doFadeOut(self, duration=5):
        bl.set_brightness(self.offLvl, smooth=True, duration=duration)
    def doOn(self):
        bl.set_brightness(255)
    def doOff(self):
        bl.set_brightness(self.offLvl)

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


if __name__ == "__main__":
    iled = IntegraLCDBack(offLvl=20)
    while True:
        iled.doOn()
        time.sleep(1)
        iled.doOff()
        time.sleep(1)
        iled.doFadeIn(duration=1)
        time.sleep(1.5)
        iled.doFadeOut(duration=1)
        time.sleep(1.5)