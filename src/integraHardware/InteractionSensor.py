if __name__ == "__main__":
    from AbstractSensor import AbstractSensor
else:
    from .AbstractSensor import AbstractSensor
from pynput.mouse import Listener
from datetime import datetime
import time
class InteractionSensor(AbstractSensor):
    
    sensor = None
    def sensorID(self):
        return "PI LCD"
    
    def __init__(self):
        AbstractSensor.__init__(self)
        self.lastClicked = datetime.now()
        self.movetimeout = 2
        listener = Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        listener.start()
        self.measurements = {
                "Interaction" : [False,""],
            }
    def reset(self):
        time.sleep(0.01)
    def on_move(self, x, y):
        self.lastClicked = datetime.now()
    def on_click(self, x, y, button, pressed):
        self.lastClicked = datetime.now()
    def on_scroll(self, x, y, dx, dy):
        self.lastClicked = datetime.now()
    def poll(self):
        self.measurements["Interaction"][0] = ((datetime.now() - self.lastClicked).seconds < self.movetimeout)
if __name__ == "__main__":
    sensor = InteractionSensor()
    while True:
        sensor.poll()
        print(sensor.measurements)
        time.sleep(1)