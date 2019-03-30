from .AbstractSensor import AbstractSensor
from smbus2 import SMBusWrapper, i2c_msg
import time
STATUS = 0X00
MEAS_MODE = 0X01
ALG_RESULT_DATA = 0X02
RAW_DATA = 0X03
ENV_DATA = 0X05
NTC = 0X06
THRESHOLDS = 0X10
BASELINE = 0X11
HW_ID = 0X20
HW_VERSION = 0X21
FW_Boot_Version = 0x23
FW_App_Version = 0x24
ERROR_ID = 0XE0
SW_RESET = 0XFF 
class CO2Tvoc(AbstractSensor):
    i2cAddr = 0x5A

    def readSensorReg(self, regAddr, numBits):
        result = []
        with SMBusWrapper(1) as bus:
            result = bus.read_i2c_block_data(self.i2cAddr, regAddr, numBits, force=True)
        return result
    
    def writeSensorReg(self, regAddr, data):
        with SMBusWrapper(1) as bus:
            bus.write_i2c_block_data(self.i2cAddr, regAddr, data, force=True)
            
    def reset(self):
        with SMBusWrapper(1) as bus:
            bus.write_byte(self.i2cAddr, 0xF4, force=True)

    def sensorID(self):
        return "CCS811"


    def __init__(self):
        AbstractSensor.__init__(self)
        self.reset()
        self.writeSensorReg(0x01, [0x10])

        self.measurements = {
            "TVOC" : [-1,"ppb"],
            "CO2" : [-1,"ppm"]
        }
        if(self.readSensorReg(STATUS,1)[0] & 0x01):
            print("Sensor returned bad status")

    def poll(self):
        try:
            status = self.readSensorReg(STATUS,1)[0]
            if ((status & 0x08)):
                vals = self.readSensorReg(ALG_RESULT_DATA,5)
                if(status & 0x01):
                    print("Error: {:02x}".format(self.readSensorReg(ERROR_ID,1)[0]))
                else:
                    self.measurements["CO2"][0] = int.from_bytes(vals[0:2], 'big', signed=False) & 0x7FFF
                    self.measurements["TVOC"][0] = int.from_bytes(vals[2:4], 'big', signed=False) & 0x7FFF
        except:
            print("Error occured")


    
