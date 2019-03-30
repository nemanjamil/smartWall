import time
import csv
import datetime
from threading import Timer

from integraHardware.WeatherSensor import WeatherSensor
from integraHardware.CO2Tvoc import CO2Tvoc
from integraHardware.MotionSensor import MotionSensor
from integraHardware.SpectralSensor import SpectralSensor

class IntegraHWManager:

    def __init__(self, autoRefresh=False, autoRefreshPeriod=1, log=False, logFilename="", logPeriod=1):
        self.sensors = [WeatherSensor(), CO2Tvoc(), SpectralSensor(), MotionSensor()]
        self.measurementSources = dict()
        self.measurementTypes = []
        for sensor in self.sensors:
            measurementTypes = sensor.getMeasurementTypes()
            for measurementType in measurementTypes:
                self.measurementSources[measurementType] = sensor
                self.measurementTypes.append(measurementType)
        self.autoRefresh = autoRefresh
        if (self.autoRefresh):
            self.interval = autoRefreshPeriod
            self.refresh()
        self.log = log
        if(self.log):
            self.logFile = logFilename
            self.logPeriod = logPeriod
            self.doLog()
    def refresh(self):
        for sensor in self.sensors:
            sensor.refresh()
        if(self.autoRefresh):
            self.t = Timer(self.interval, self.refresh)
            self.t.daemon = True
            self.t.start()
    def getMeasurementValue(self, meastype):
        sensor = self.measurementSources[meastype]
        return sensor.getMeasurementValue(meastype)
    def getMeasurementTypes(self):
        return self.measurementTypes
    def getMeasurementUnit(self, meastype):
        return self.measurementSources[meastype].getMeasurementUnit(meastype)
    def getAllMeasurementVals(self):
        measurementVals = []
        for measurement in self.getMeasurementTypes():
            measurementVals.append(self.getMeasurementValue(measurement))
        return measurementVals
    def doLog(self):
        print("Logging")
        with open(self.logFile, "a") as outFile:
            writer = csv.writer(outFile)
            towrite = [datetime.datetime.now(), self.getAllMeasurementVals()]
            writer.writerow(towrite)
        if(self.log):
            self.logt = Timer(self.logPeriod, self.doLog)
            self.logt.daemon = True
            self.logt.start()

if __name__ == "__main__":
    hwmgr = IntegraHWManager(autoRefresh=True, autoRefreshPeriod=1.0, log=True, logPeriod=5.0, logFilename="Measurements log")

    while True:
        print(hwmgr.getMeasurementValue("Motion"))
        time.sleep(0.5)