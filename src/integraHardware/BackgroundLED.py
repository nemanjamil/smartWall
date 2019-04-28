from .AbstractLEDController import AbstractLEDController
from .IntegraLED import IntegraLED

class BackgroundLED(AbstractLEDController):
    def __init__(self, getMeasurementCallback):
        AbstractLEDController.__init__(self,
        LED=IntegraLED("GPIO27"),
        getMeasurementCallback=getMeasurementCallback,
        fading=True, 
        fadingInterval=5,
        offDelay=True, 
        offDelayPeriod=8)
        self.threshold = 20 # lux
    def processMeasurement(self, measurement):
        res = (measurement["LUX"]["value"] < self.threshold) | (measurement["Motion"]["value"])
        return res


