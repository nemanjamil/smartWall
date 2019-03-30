from .AbstractSensor import AbstractSensor
import gpiozero
import time
class MotionSensor(AbstractSensor):
    
    sensor = None
    def sensorID(self):
        return "PIR500B"
    
    def __init__(self):
        AbstractSensor.__init__(self)
        self.sensor = gpiozero.MotionSensor("GPIO4")
        self.measurements = {
                "Motion" : [False,""],
            }
    def poll(self):
        self.measurements["Motion"][0] = self.sensor.motion_detected

