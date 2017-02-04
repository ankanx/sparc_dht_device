import sys
sys.path.append('../lib')
import Adafruit_DHT

# Sensor class
class Sensor:
     def __init__(self, parent):
         self.parent = parent

     # Takes a reading from the sensors and returns the values
     def take_reading():
          humidity, temperature = Adafruit_DHT.read_retry(11, 4)
          return humidity,temperature;
