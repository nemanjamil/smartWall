from sensor import AbstractSensor
import bme280
from smbus2 import SMBusWrapper
import time
class WeatherSensor(AbstractSensor):
    i2cAddr = 0x76
    measurements = {
        "temperature" : [-1,"&#x2103"],
        "pressure" : [-1,"mbar"],
        "humidity" : [-1,"%"]
    }
    calib_params = None
    def sensorID(self):
        return "BME280"
    def getMeasurementValue(self, type):
        return self.measurements[type]

    def getMeasurementTypes(self):
        return list(self.measurements.keys)
    def getMeasurementUnit(self, type):
        return self.measurements[type][1]
    def __init__(self):
        with SMBusWrapper(1) as bus:
            self.calib_params = bme280.load_calibration_params(bus, self.i2cAddr)
        
    def poll(self):
        with SMBusWrapper(1) as bus:
            data = bme280.sample(bus, self.i2cAddr, self.calib_params)
            self.measurements["temperature"][0] = data.temperature
            self.measurements["pressure"][0] = data.pressure
            self.measurements["humidity"][0] = data.humidity
