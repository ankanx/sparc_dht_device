#!/bin/bash

#Install the sparc_htm dependencies
echo "Starting the sparc_dht_device setup..."
sudo apt-get update
sudo apt-get install git-core
sudo apt-get install python-dev
sudo apt-get install build-essential
sudo pip install paho-mqtt

#Clone and install the DHT11 library
echo ""
echo "Starting DHT11 library intsall......"
echo ""
echo ""
echo "Moving into \"publisher\" directory......"
echo ""
cd application/lib/
echo ""
echo "Cloning repository......"
echo ""
sudo  git clone https://github.com/adafruit/Adafruit_Python_DHT.git
echo ""
echo "Moving into \"Adafruit_python_DHT\" directory......"
echo ""
cd Adafruit_Python_DHT
echo ""
echo "Running install......"
echo ""
sudo python setup.py install
cd ../../

#Generate Node UUUID
echo ""
echo "Generating UUID..."
echo ""
cd settings/
sudo python setup.py
cd ../../

#Install the sparc_htm startup service
echo ""
echo "Starting service install......"
echo ""
echo ""
echo "Moving into \"systemd\" directory......"
echo ""
cd setup/systemd/
echo ""
echo "Copying service into \"/lib/systemd/system/ ......"
echo ""
sudo cp sparc_htm.service /lib/systemd/system/
cd ../
echo ""
echo "Enabling sparc_htm service......"
echo ""
sudo systemctl enable sparc_htm.service
echo ""
echo "Reloading systemctl daemon...."
echo ""
sudo systemctl daemon-reload
echo ""
echo "Starting sparc_htm service......"
echo ""
sudo systemctl start sparc_htm.service
echo ""
echo "Checking sparc_htm service status......"
echo ""
sudo systemctl status sparc_htm.service

#Install the autoconnecting wifi
echo ""
echo "Starting Wifi Config......"
echo ""
echo "Shutting Down Wlan0...."
sudo ifdown Wlan0
echo ""
echo "Moving into \"/rpi/network/\"......"
echo ""
cd network/
echo ""
echo "Copying interface config to \"/etc/network/\"......"
echo ""
sudo cp interfaces /etc/network/
echo ""
echo "Starting wlan0 again......"
echo ""
sudo ifup wlan0
echo "Setup complete....please check for failures... singular modules failing does not stop the configuration..."
