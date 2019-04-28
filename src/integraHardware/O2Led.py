from .AbstractLEDController import AbstractLEDController
from .IntegraLED import IntegraLED

class O2Led(AbstractLEDController):
    def __init__(self, getMeasurementCallback):
        AbstractLEDController.__init__(self,
        LED=IntegraLED("GPIO22"),
        getMeasurementCallback=getMeasurementCallback,
        fading=True, 
        fadingInterval=1,
        offDelay=True, 
        offDelayPeriod=5)
        self.threshold = 19 # %
    def processMeasurement(self, measurement):
        return measurement["O2"]["value"] < self.threshold


