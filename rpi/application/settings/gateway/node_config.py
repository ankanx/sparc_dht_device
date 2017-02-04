import paho.mqtt.client as mqtt
import json
import time
# The callback for when the client receives a CONNACK response from the
# server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    

# if disconnected reconnnect to host
def on_disconnect(client, userdata, rc):
    print "Lost connection, trying to reestablish connection....."
    client.reconnect()

# Looping connection establisher
def force_connection(client):
    try:
        client.connect("192.168.10.1", 1883, 60)
    except:
        print "Could not connect... trying to reconnect"
        time.sleep(5)
        force_connection(client)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    publish_data(client)

def publish_data(client):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    payload = {
	??
    }
    client.publish("SPARC/home_automation/config", json.dumps(payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
print "Trying to establish innitial connection..."
force_connection(client)
 
client.loop_forever()
