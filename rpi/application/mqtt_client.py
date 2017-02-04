import paho.mqtt.client as mqtt
import re
import time
import settings.file_manager

class MQTTClient:
    def __init__(self, broker, is_local, parent,serial_number):
        self.parent = parent
        self.broker = broker
        self.client = mqtt.Client()
        global client 
        client= self.client 
        self.client.will_set('SPARC/home_automation/disconnect/' + serial_number,'Last Will',0,False)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        
        # Start the connection cycle
        
        print "Trying to establish innitial connection...."    
        self.connect(client,broker)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.client.loop_start()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Broker on " + self.broker + ", connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
    
    # The callback for when client gets disconnected from server
    def on_disconnect(self, client, userdata, rc):
        print "Lost connection.. trying to reconnect"
        self.client.reconnect()

    # Connect function trying until connection has been established.
    def connect(self,client,broker):
        try:
            print "Connecting to" + broker
            self.client.connect(broker, 1883, 60)    
        except:
            time.sleep(5)
            print "Connection reached an exception... trying to reconnect"
            self.connect(client,broker)

    def on_message(self, client, userdata, message):
        self.parent.publish()
        ###########

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, payload=None):
        if payload is None:
            self.client.publish(topic)
        else:
            self.client.publish(topic, payload)
