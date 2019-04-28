from .AbstractLEDController import AbstractLEDController
from .IntegraLED import IntegraLED

class DustLed(AbstractLEDController):
    def __init__(self, getMeasurementCallback):
        AbstractLEDController.__init__(self,
        LED=IntegraLED("GPIO6"),
        getMeasurementCallback=getMeasurementCallback,
        fading=True, 
        fadingInterval=1,
        offDelay=True, 
        offDelayPeriod=5)
        self.threshold = 25 # %
    def processMeasurement(self, measurement):
        return measurement["temperature"]["value"] > self.threshold


