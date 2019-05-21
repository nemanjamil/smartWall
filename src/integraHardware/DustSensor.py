if __name__ == "__main__":
    from AbstractSensor import AbstractSensor
else:
    from .AbstractSensor import AbstractSensor
import serial
import time
from threading import Lock
from threading import Timer
from enum import Enum
class DustSensor(AbstractSensor):
    
    sensor = None
    def sensorID(self):
        return "SDS011"
    class state(Enum):
        waitStart = 0,
        waitCommID = 1,
        gettingData = 2,
        waitChecksum = 3,
        waitEnd = 4

    def __init__(self):
        AbstractSensor.__init__(self)
        self.serial = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
        
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()
        self.odbuf = [0] * 6
        self.intermediatePoll = 0.2
        self.lock = Lock()
        #self.lock.release()
        self.currentState = self.state.waitStart
        self.measurements = {
                "PM10" : [-1,"<sup>&mu;g</sup>&frasl;<sub>m<sup>3</sup></sub>"],
                "PM2.5" : [-1,"<sup>&mu;g</sup>&frasl;<sub>m<sup>3</sup></sub>"]
            }
        self.t = Timer(self.intermediatePoll, self.pollSerial)
        self.t.daemon = True
        self.t.start()
    def reset(self):
        time.sleep(0.01)
    def poll(self):
        self.lock.acquire()
        self.measurements["PM2.5"][0] = (self.odbuf[0] + (self.odbuf[1] << 8)) / 10
        self.measurements["PM10"][0] = (self.odbuf[2] + (self.odbuf[3] << 8)) / 10
        self.lock.release()
    def pollSerial(self):
        while(self.serial.in_waiting > 0):
            inDat = ord(self.serial.read())
            if(self.currentState == self.state.waitStart):
                self.dbuf = []
                if(inDat == 0xAA):
                    self.currentState = self.state.waitCommID
            elif(self.currentState == self.state.waitCommID):
                if(inDat == 0xC0):
                    self.currentState = self.state.gettingData
                else:
                    self.currentState = self.state.waitStart
            elif(self.currentState == self.state.gettingData):
                self.dbuf.append(inDat)
                if(len(self.dbuf) == 6):
                    self.currentState = self.state.waitChecksum
            elif(self.currentState == self.state.waitChecksum):
                if(sum(self.dbuf) % 256 == inDat):
                    self.currentState = self.state.waitEnd
                else:
                    self.currentState = self.state.waitStart
            elif(self.currentState == self.state.waitEnd):
                if(inDat == 0xAB):
                    self.lock.acquire()
                    self.odbuf = self.dbuf
                    self.lock.release()
                self.currentState = self.state.waitStart
        self.t = Timer(self.intermediatePoll, self.pollSerial)
        self.t.daemon = True
        self.t.start()
if __name__ == "__main__":
    sensor = DustSensor()
    while True:
        sensor.poll()
        print(sensor.measurements)
        time.sleep(2)