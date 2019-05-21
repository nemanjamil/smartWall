from .AbstractLEDController import AbstractLEDController
from .IntegraLCDBack import IntegraLCDBack

class BacklightLCD(AbstractLEDController):
    def __init__(self, getMeasurementCallback):
        AbstractLEDController.__init__(self,
        LED=IntegraLCDBack(offLvl=15),
        getMeasurementCallback=getMeasurementCallback,
        fading=True, 
        fadingInterval=1,
        offDelay=True, 
        offDelayPeriod=1800)
        
    def processMeasurement(self, measurement):
        res = (measurement["Motion"]["value"]) | (measurement["Interaction"]["value"])
        return res


