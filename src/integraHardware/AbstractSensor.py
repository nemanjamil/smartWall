## @file sensor.py
#  @brief Contains abstract class definition for sensor interfacing

#  This will be used throughout sensors
import threading

## @brief Abstract class used
#  for sensor interfacing
#
#  Contains methods and properties which should
#  be implemented by all of the sensors
class AbstractSensor:
        
    def __init__(self):
        self.measurementSem = threading.Lock()
        self.measurements = None
    

    def reset(self):
        pass
    def performReset(self):
        self.measurementSem.acquire()
        self.reset()
        self.measurementSem.release()
    @property
    ## This contains the product code of 
    #  currently used sensor
    def sensorID(self):
        pass

    ## @brief Measure the value determined by string
    #  `type`
    #
    #  @param type Sensor-specific string determining 
    #  the measurement type for the sensor
    def getMeasurementValue(self, type):
        res = -1
        self.measurementSem.acquire()
        try:
            res = self.measurements[type]
            res = res[0]
        except:
            print("Measurement not available")
        self.measurementSem.release()
        return res

    ## List all possible measurement types
    #
    #  Returns a list of string containing measurement
    #  types
    def getMeasurementTypes(self):
        return list(self.measurements.keys())
    
    ## Get the unit of measure for the given
    #  measurement type
    #
    #  @param type Sensor-specific string determining
    #  the measurement type for the sensor
    def getMeasurementUnit(self, type):
        return self.measurements[type][1]
    
    ## Pull register values from the sensor
    #  and store them locally
    def poll(self):
        pass

    ## Perform a thread-safe refresh of the 
    #  measurements 
    def refresh(self):
        self.measurementSem.acquire()
        try:
            self.poll()
        except Exception as e:
            print("An error during poll occured", str(e))
        self.measurementSem.release()
        

    ## Returns the sensor description in human
    #  readable form. This can be used for debug and 
    #  for presenting to the user
    def getHumanReadableDescription(self):
        return """This is a {0} sensor interface. 
Possible measurement types are {1}""".format(self.sensorID, self.getMeasurementTypes)


