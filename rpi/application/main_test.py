# Internal
from mqtt_client import MQTTClient
import json
#import lib.Adafruit_DHT
import time
import settings.file_manager
#import payload.sensor
class Main:
    def __init__(self):
        global node_settings
        global node_identity
        node_settings = settings.file_manager.load_factory_settings()
        node_identity = settings.file_manager.load_settings()
      #  self.sensor = payload.sensor.Sensor(self)
        self.client = MQTTClient("prata.technocreatives.com", False, self)
        self.client.subscribe("SPARC/home_automation/123e4567-e89b-12d3-a456-426655440000/readall")

        print "\nStarting to publish sensor data with a 5 second interval..."
        
        self.publish()
        while True:
            time.sleep(5)
            self.publish()

    def publish(self):
         # Take one sensor reading
 #       humidity,temperature = self.sensor.take_reading()
        humidity = 11
        temperature = 12      
        # Payload construction
        payload = {
            "ts": time.time(),
            "type": node_identity["type"],
            "name": node_identity["name"],
            "serial_number": node_settings["serial_number"],
            "location": node_identity["location"],
            "temperature": temperature,
            "humidity": humidity
        }
        self.client.publish("SPARC/home_automation/123e4567-e89b-12d3-a456-426655440000/info/" + node_settings["serial_number"], json.dumps(payload))

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))


if __name__ == "__main__":
    main = Main()
