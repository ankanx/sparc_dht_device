import paho.mqtt.client as mqtt
import json

config = {}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("SPARC/home_automation/config")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print "Message received"
    load_config()
    print str(msg.payload)
    payload = json.loads(str(msg.payload))
    for key in payload:
        config[key] = payload[key]
    save_config()


def load_config():
    global config
    for line in open('config', 'r'):
        line.strip()
        key, value = line.split(':')
        value = value.strip(' \n\t\r')
        print key + ": " + value + "\n"
        config[key] = value

# TODO(Daniel): Unsafe save, will overwrite the config file with whatever is
#   loaded into the config dct. Possible solution could be save to different file and if
#   errorless swith the config file for the temp.
def save_config():
    global config
    with open('config', 'w') as file:
        for key in config:
            print "Save " +config[key]
            file.write(key + ': ' + config[key] + '\n')

load_config()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
