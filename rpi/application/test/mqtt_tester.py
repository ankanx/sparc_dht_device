import paho.mqtt.client as mqtt
import json
import time
# The callback for when the client receives a CONNACK response from the
# server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection
    # and reconnect then subscriptions will be renewed.
    client.subscribe("SPARC/home_automation/readall")

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

# The publishing function
def publish_data(client):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    payload = {
        "payload": "tests"
    }
    client.publish("SPARC/home_automation/info/c607a0e0-2a24-42d6-bb66-926152215027", json.dumps(payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
# Start connection cycle
print "Trying to establish innitial connection..."
force_connection(client)

 

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting. Other loop*() functions are available that give
# a threaded interface and a manual interface.

timer = time.time()
while True:
    client.loop()
    if time.time() > timer + 5:
        timer = time.time()
        publish_data(client)
