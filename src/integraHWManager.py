## @file integraHWManager.py
#  @brief High-level interface to sensors implemented
#  in integraHardware

import time
import csv
from datetime import datetime
from threading import Timer
import os
from integraHardware.WeatherSensor import WeatherSensor
from integraHardware.CO2Tvoc import CO2Tvoc
from integraHardware.MotionSensor import MotionSensor
from integraHardware.SpectralSensor import SpectralSensor
from integraHardware.O2Sensor import O2Sensor
from integraHardware.DustSensor import DustSensor
from integraHardware.InteractionSensor import InteractionSensor

from integraHardware.CO2Led import CO2Led
from integraHardware.BackgroundLED import BackgroundLED
from integraHardware.O2Led import O2Led
from integraHardware.DustLed import DustLed
from integraHardware.BacklightLCD import BacklightLCD
class IntegraHWManager:

    def __init__(self, autoRefresh=False, autoRefreshPeriod=1, log=False, logFilename="", logPeriod=1):
        
        # Initialize the sensors and prepare the data structures holding them
        self.sensors = [ WeatherSensor(), 
                         CO2Tvoc(), 
                         SpectralSensor(), 
                         MotionSensor(), 
                         O2Sensor(),
                         DustSensor(),
                         InteractionSensor()
                        ]
        self.leds = [ CO2Led(self.getAllDicts), 
                      BackgroundLED(self.getAllDicts), 
                      O2Led(self.getAllDicts),
                      DustLed(self.getAllDicts),
                      BacklightLCD(self.getAllDicts)
                    ]
        self.measurementSources = dict()
        self.dicts = dict()
        self.measurementTypes = []
        self.resetInterval = 60
        self.reset()

        # Initialize connections with sensors
        for sensor in self.sensors:
            measurementTypes = sensor.getMeasurementTypes()
            for measurementType in measurementTypes:
                self.measurementSources[measurementType] = sensor
                self.measurementTypes.append(measurementType)
        
        # If refreshing is performed automatically (preferred)
        # initialize the refresh routines and start
        self.autoRefresh = autoRefresh
        

        if (self.autoRefresh):
            self.interval = autoRefreshPeriod
            self.refresh()
        self.log = log
        if(self.log):
            self.logPeriod = logPeriod
        # If logging is enabled, build log file 
        # and start logging
        self.reInitLogfile(logFilename)
    
    ## @brief Init a logfile and start logging
    def reInitLogfile(self, logFilename):
        if(self.log):
            self.logFile = logFilename
            with open(self.logFile,"w") as fileHandle:
                writer = csv.writer(fileHandle)
                measurements = self.measurementTypes
                writer.writerow(measurements + ["Datetime"])
            self.doLog()
    ## @brief Do a refresh of all sensors
    def refresh(self):
        # Go through all of the sensors and perform
        # a refresh
        for sensor in self.sensors:
            sensor.refresh()
        
        self.refreshAllDicts()

        # Perform LED updates
        for led in self.leds:
            led.refresh()

        # Init next thread if auto refresh enabled
        if(self.autoRefresh):
            self.t = Timer(self.interval, self.refresh)
            self.t.daemon = True
            self.t.start()
        
    def reset(self):
        for sensor in self.sensors:
            sensor.performReset()
        self.tReset = Timer(self.resetInterval, self.reset)
        self.tReset.daemon = True
        self.tReset.start()    
    ## @brief Acquire the measurement value
    # using the joined measurement types
    def getMeasurementValue(self, meastype):
        sensor = self.measurementSources[meastype]
        return sensor.getMeasurementValue(meastype)
    
    # Get the list of available measurement types
    def getMeasurementTypes(self):
        return self.measurementTypes
    
    # Get the string value of the measurement unit
    def getMeasurementUnit(self, meastype):
        return self.measurementSources[meastype].getMeasurementUnit(meastype)

    # Acquire a list of all measurement values
    # in order determined by getMeasurementTypes()
    def getAllMeasurementVals(self):
        measurementVals = []
        for measurement in self.getMeasurementTypes():
            measurementVals.append(self.getMeasurementValue(measurement))
        return measurementVals

    def refreshAllDicts(self):
        types = self.getMeasurementTypes()
        res = dict()
        for type in types:
            typeRes = dict()
            typeRes["unit"] = self.getMeasurementUnit(type)
            typeRes["value"] = self.getMeasurementValue(type)
            res[type] = typeRes
        self.dicts = res

    def getAllDicts(self):
        return self.dicts


    # Perform a logging operation
    def doLog(self):
        with open(self.logFile, "a") as outFile:
            writer = csv.writer(outFile)
            towrite = self.getAllMeasurementVals()
            stringVals = list(str(e) for e in towrite)
            stringVals.append(datetime.now().strftime("%d.%m.%Y. %H:%M:%S"))
            writer.writerow(stringVals)
        if(self.log):
            self.logt = Timer(self.logPeriod, self.doLog)
            self.logt.daemon = True
            self.logt.start()

if __name__ == "__main__":
    hwmgr = IntegraHWManager(autoRefresh=True, autoRefreshPeriod=1.0, log=True, logPeriod=5.0, logFilename="log.txt")

    while True:
        print(hwmgr.getMeasurementValue("Motion"))
        time.sleep(0.5)