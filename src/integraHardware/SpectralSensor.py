from .AbstractSensor import AbstractSensor
from smbus2 import SMBusWrapper, i2c_msg
import time
import struct

STATUS = 0x00
WRITE = 0x01
READ = 0x02

V_HW_Version_l = 0x00
V_HW_Version_h = 0x01

V_FW_Version_l = 0x02
V_FW_Version_h = 0x03

V_Control_Setup = 0x04
V_INT_T = 0x05
V_Device_Temp = 0x06
V_LED_Control = 0x07

V_X_High = 0x08
V_X_Low = 0x09

V_Y_High = 0x0A
V_Y_Low = 0x0B

V_Z_High = 0x0C
V_Z_Low = 0x0D

V_NIR_High = 0x0E
V_NIR_Low = 0x0F

V_Dark_High = 0x10
V_Dark_Low = 0x11

V_Clear_High = 0x12
V_Clear_Low = 0x13

V_F_Cal_X = 0x14
V_F_Cal_Y = 0x18
V_F_Cal_Z = 0x1C

V_F_Cal_x_1931 = 0x20
V_F_Cal_y_1931 = 0x24

V_F_Cal_upri = 0x28
V_F_Cal_vpri = 0x2C

V_F_Cal_u = 0x30
V_F_Cal_v = 0x34

V_F_Cal_DUV = 0x38
V_Cal_LUX = 0x3C
V_Cal_CCT = 0x40


class SpectralSensor(AbstractSensor):
    i2cAddr = 0x49


    
    def bytesToFloat(self, byteList):
        return struct.unpack(">f", bytes(byteList))[0]

    def writeVirtualReg(self, register, value):
        with SMBusWrapper(1) as bus:
            while(bus.read_byte_data(self.i2cAddr, STATUS) & 0x02):
                time.sleep(0.01)
            bus.write_byte_data(self.i2cAddr, WRITE, register | 0x80)
            while(bus.read_byte_data(self.i2cAddr, STATUS) & 0x02):
                time.sleep(0.01)
            bus.write_byte_data(self.i2cAddr, WRITE, value)

    
    def readVirtualReg(self, register):
        with SMBusWrapper(1) as bus:
            while bus.read_byte_data(self.i2cAddr, STATUS) & 0x02:
                time.sleep(0.01)
            bus.write_byte_data(self.i2cAddr, WRITE, register)
            while not(bus.read_byte_data(self.i2cAddr, STATUS) & 0X01):
                time.sleep(0.01)
            return bus.read_byte_data(self.i2cAddr, READ)


    def readFloatReg(self, registerOffset):
        res = []
        for i in range(4):
            res += [self.readVirtualReg(registerOffset + i)]
        return self.bytesToFloat(res)

    def read4byteReg(self, registerOffset):
        res = []
        for i in range(4):
            res += [self.readVirtualReg(registerOffset + i)]
        return struct.unpack(">L", bytes(res))[0]
        
    
    def sensorID(self):
        return "AS7261"



    def __init__(self):    
        AbstractSensor.__init__(self)
        self.measurements = {
            "Color temperature" : [-1,"K"],
            "DUV" : [-1, ""],
            "LUX" : [-1, "lx"] 
        }
        self.writeVirtualReg(V_LED_Control, 0x00)
        oldControl = self.readVirtualReg(V_Control_Setup)
        newControl = oldControl & ~0x30
        newControl = oldControl | 0x30
        
        self.writeVirtualReg(V_Control_Setup, newControl)

    def poll(self):
        try:
            oldControl = self.readVirtualReg(V_Control_Setup)
            self.writeVirtualReg(V_Control_Setup, oldControl | 0x0C)
            while (~(self.readVirtualReg(V_Control_Setup)) & 0x02):
                time.sleep(0.05)
            
            x = self.readFloatReg(V_F_Cal_x_1931)
            y = self.readFloatReg(V_F_Cal_y_1931)
            lux = float(self.read4byteReg(V_Cal_LUX))/50000.0

            if((x > 1.0) | (x < 0.0) | (y > 1.0) | (y < 0.0)):
                return
            
            n = (x - 0.3320) / (0.1858 - y)
            cct = 437*n**3 + 3601 * n ** 2 + 6861 * n + 5517
            self.measurements["Color temperature"][0] = cct
            self.measurements["DUV"][0] = self.readFloatReg(V_F_Cal_DUV)
            self.measurements["LUX"][0] = lux
        except:
            print("An error occured")

