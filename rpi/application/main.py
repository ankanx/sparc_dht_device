# Internal
from mqtt_client import MQTTClient
import json
import Adafruit_DHT
import time
import settings.file_manager
import payload.sensor
class Main:
    def __init__(self):
        global node_settings
        global node_identity
        node_settings = settings.file_manager.load_factory_settings()
        node_identity = settings.file_manager.load_settings()
        self.sensor = payload.sensor.Sensor(self)
        self.client = MQTTClient("192.168.10.1", False, self,node_settings["serial_number"])

        print "Publishing Device Info.."
        self.deviceInfo()


        print "\nStarting to publish sensor data with a 5 second interval..."
        while True:
            # Publish Data every 2 seconds.
            time.sleep(2)
            self.publish()


    def deviceInfo(self):
        payload = {
            "type": node_identity["type"],
            "name": node_identity["name"],
            "serial_number": node_settings["serial_number"],
            "location": node_identity["location"],
	    "info":{
		"humidity":"float",
		"temperature":"float"
	    }
        }
        self.client.publish("SPARC/home_automation/disconnect/" + node_settings["serial_number"], json.dumps(payload))




    def publish(self):
         # Take one sensor reading
        humidity,temperature = self.sensor.take_reading()
        # Payload construction
        payload = {
            "ts": time.time(),
            "serial_number": node_settings["serial_number"],
	    "values":{
            "temperature": temperature,
            "humidity": humidity
	    }
        }
        self.client.publish("SPARC/home_automation/info/" + node_settings["serial_number"], json.dumps(payload))

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))


if __name__ == "__main__":
    main = Main()
