if __name__ == "__main__":
    from AbstractSensor import AbstractSensor
else:
    from .AbstractSensor import AbstractSensor

from spidev import SpiDev
import gpiozero
import struct
import time
import csv
from os import path
from scipy.interpolate import interp1d
class O2Sensor(AbstractSensor):
    def generateCalibCurve(self):
        calibFilename = "callibCurve.csv"
        calibFile = open(path.dirname(__file__) + "/" + calibFilename, 'r')
        reader = csv.reader(calibFile)
        xVals = []
        yVals = []
        for row in reader:
            yVals.append(float(row[0]))
            xVals.append(float(row[1]))
        calibFile.close()
        self.calibF = interp1d(xVals, yVals)
        self.calibC = 92.8009950249
        self.maxOut = max(yVals)
    def __init__(self):
        AbstractSensor.__init__(self)
        self.measurements = {
            "O2" : [-1,"%"],
            "O2voltage" : [-1,"V"],    
        }
        self._spi = SpiDev(0,0)
        self._CS = gpiozero.DigitalOutputDevice(5, initial_value=True)
        #self._MISO = gpiozero.DigitalInputDevice(9)
        self._spi.open(0,0)
        self._spi.max_speed_hz = 500
        self._spi.no_cs = True
        self.generateCalibCurve()

    def poll(self):
        self._CS.value = False
        time.sleep(0.09)
        res = self._spi.readbytes(3)
        self._CS.value = True
        res[0] &= 0x1F
        resval = 0
        for i in range(3):
            resval += res[i] << (2-i)*8
        if res[0] & 0x10:
            resval =  0x0FFFFF - resval - 1
        resval = resval / float(0x0FFFFF) * 3.3
        self.measurements["O2voltage"][0] = resval
        try:
            concentration = float(self.calibF(resval * self.calibC).item(0))
            self.measurements["O2"][0] = concentration
        except:
            self.measurements["O2"][0] = self.maxOut
if __name__ == "__main__":

    o2sens = O2Sensor()
    while True:
        o2sens.poll()
        print(o2sens.measurements)
        time.sleep(0.05)

