from sensor import AbstractSensor
import gpiozero
import time
class MotionSensor(AbstractSensor):
    
    sensor = None
    def sensorID(self):
        return "PIR500B"
    def getMeasurementValue(self, type):
        return self.measurements[type]

    def getMeasurementTypes(self):
        return list(self.measurements.keys)
    def getMeasurementUnit(self, type):
        return self.measurements[type][1]
    def __init__(self):
        AbstractSensor.__init__(self)
        self.sensor = gpiozero.MotionSensor("GPIO4")
        self.measurements = {
                "Motion" : [-1,""],
            }
    def poll(self):
        self.measurements["Motion"] = self.sensor.motion_detected

sens = MotionSensor()
while True:
    sens.refresh()
    print(sens.getMeasurementValue("Motion"))
    time.sleep(0.1)