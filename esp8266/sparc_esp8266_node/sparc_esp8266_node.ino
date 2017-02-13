/*

  SPARC - Esp 8266 Node
  @author Andreas FRansson

  Dependency: change the PubSubClient maximum package size from 128 to 250.

*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#include <ArduinoJson.h>

const char* ssid = "SPARC";
const char* password = "SPARC1337";
const char* mqtt_server = "192.168.10.1";
#define DHTPIN 2  
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

WiFiClient espClient;
PubSubClient client(espClient);

long lastMsg = 0;
int value = 0;
String serial_number = "3469b939-cf00-430e-a3ff-8c2c5e82a142";
String topic_device = "SPARC/home_automation/disconnect/"+serial_number;
String topic_info = "SPARC/home_automation/info/"+serial_number;
char device_topic[80];
char info_topic[80];


void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  dht.begin();

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
   
    String clientId = "SPARC_THM - ESP8266";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...

      char data[190];

      String payload = "{\"type\": \"Temperature Humidity Sensor\",\"name\": \"demo\", \"serial_number\": "+ serial_number +", \"location\": \"demo\",\"info\":{ \"humidity\":\"float\",\"temperature\":\"float\" }";
      payload.toCharArray(data, (payload.length() + 1));
      Serial.println(payload);
      Serial.println(payload.length());
      client.publish(device_topic,data);
 
      
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {

  // Setup topics
  topic_device.toCharArray(device_topic, (topic_device.length() + 1));
  topic_info.toCharArray(info_topic, (topic_info.length() + 1));

  
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 2000) {
    
    lastMsg = now;

    // Take a new reading from the sensor.
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    // Package size
    char data[150];

    // Payload
    String payload = "{\"ts\":" + (String)millis() +",\"serial_number\": "+ serial_number +",\"values\":{\"temperature\": "+ (String)t +",\"humidity\": "+(String)h+"}} ";
    // Make Payload delivereble.
    payload.toCharArray(data, (payload.length() + 1));
    
    //Serial.print("Publish message: ");
    //Serial.println(payload.length());

    // Publish to topic
    client.publish(info_topic, data);
    //Serial.println(payload);
  }
}
