from .AbstractLEDController import AbstractLEDController
from .IntegraLED import IntegraLED

class CO2Led(AbstractLEDController):
    def __init__(self, getMeasurementCallback):
        AbstractLEDController.__init__(self,
        LED=IntegraLED("GPIO17"),
        getMeasurementCallback=getMeasurementCallback,
        fading=True, 
        fadingInterval=1,
        offDelay=True, 
        offDelayPeriod=5)
        self.threshold = 1000 # ppm
    def processMeasurement(self, measurement):
        return measurement["CO2"]["value"] > self.threshold


