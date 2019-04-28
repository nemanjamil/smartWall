from .IntegraLED import IntegraLED
from abc import ABC, abstractmethod
from datetime import datetime

class AbstractLEDController:
    def __init__(self, LED, getMeasurementCallback, fading=False, fadingInterval=1, offDelay=False, offDelayPeriod=10):
        self.LED = LED
        self.measurementCallback = getMeasurementCallback
        self.lastOn = datetime.now()
        self.offDelay = offDelay
        self.offDelayPeriod = offDelayPeriod
        self.fading = fading
        self.fadingInterval = fadingInterval

    
    @abstractmethod
    def processMeasurement(self, value):
        pass

    def refresh(self):
        measurement = self.measurementCallback()
        isOn = self.processMeasurement(measurement)
        if self.offDelay:
            if isOn:
                self.lastOn = datetime.now()
            else:
                if (datetime.now() - self.lastOn).seconds > self.offDelayPeriod:
                    isOn = False
                else:
                    isOn = True
        if self.fading:
            self.LED.doFade(isOn, self.fadingInterval)
        else:
            self.LED.doImmediateSwitch(isOn)
        
            