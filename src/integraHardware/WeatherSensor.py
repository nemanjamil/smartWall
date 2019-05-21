from .AbstractSensor import AbstractSensor
import bme280
from smbus2 import SMBusWrapper
import time
class WeatherSensor(AbstractSensor):
    i2cAddr = 0x76

    calib_params = None
    def sensorID(self):
        return "BME280"


    def __init__(self):
        AbstractSensor.__init__(self)
        self.measurements = {
            "temperature" : [-1,"&#8451;"],
            "pressure" : [-1,"mbar"],
            "humidity" : [-1,"%"]
        }
        with SMBusWrapper(1) as bus:
            self.calib_params = bme280.load_calibration_params(bus, self.i2cAddr)
    
    def reset(self):
        time.sleep(0.01)

    def poll(self):
        with SMBusWrapper(1) as bus:
            data = bme280.sample(bus, self.i2cAddr, self.calib_params)
            self.measurements["temperature"][0] = data.temperature
            self.measurements["pressure"][0] = data.pressure
            self.measurements["humidity"][0] = data.humidity
