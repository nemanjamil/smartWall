## @file sensor.py
#  @brief Contains abstract class definition for sensor interfacing

#  This will be used throughout sensors
import asyncio

## @brief Abstract class used
#  for sensor interfacing
#
#  Contains methods and properties which should
#  be implemented by all of the sensors
class AbstractSensor:
        
    def __init__(self):
        self.measurementSem = asyncio.Semaphore()

    @property
    ## This contains the product code of 
    #  currently used sensor
    def sensorID(self):
        pass

    measurements = None
    measurementSem = None
    ## @brief Measure the value determined by string
    #  `type`
    #
    #  @param type Sensor-specific string determining 
    #  the measurement type for the sensor
    def getMeasurementValue(self, type):
        res = -1
        self.measurementSem.acquire()
        res = self.measurements[type]
        self.measurementSem.release()
        return res

    ## List all possible measurement types
    #
    #  Returns a list of string containing measurement
    #  types
    def getMeasurementTypes(self):
        pass
    
    ## Get the unit of measure for the given
    #  measurement type
    #
    #  @param type Sensor-specific string determining
    #  the measurement type for the sensor
    def getMeasurementUnit(self, type):
        pass
    
    ## Pull register values from the sensor
    #  and store them locally
    def poll(self):
        pass

    ## Perform a thread-safe refresh of the 
    #  measurements 
    def refresh(self):
        self.measurementSem.acquire()
        self.poll()
        self.measurementSem.release()
        
    
    ## Returns the sensor description in human
    #  readable form. This can be used for debug and 
    #  for presenting to the user
    def getHumanReadableDescription(self):
        return """This is a {0} sensor interface. 
Possible measurement types are {1}""".format(self.sensorID, self.getMeasurementTypes)


