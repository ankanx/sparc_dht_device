#Configure service on gateway

To use the injecttion script do the follwoing:
-------------------------------------------------------------------------

1. chmod u+x inject.sh

2. ./inject.sh

3. follow instructions

To inject configuration direcly into broker and manually configure a node use the following

EX:
--------------------------------------------------------------------------
mosquitto_pub -t SPARC/home_automation/config -m "{\"name\":\"Bjorn\"}"

Dependencies for the broker:
--------------------------------------------------------------------------

1. sudo apt-get install mosquitto
(Only if you want to inject messages)
2. sudo apt-get install mosquitto-clients
