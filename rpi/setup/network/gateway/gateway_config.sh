#!/bin/bash

# Can be found here for manual config:
#http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/

#Configure wifi as host
echo ""
echo "Starting configure pi as sparc_gateway wifi host...."
echo ""
echo "Installing dhcp server..."
echo ""
sudo apt-get install isc-dhcp-server
echo ""
echo "Cloning hostapd configuration..."
echo ""
wget https://github.com/jenssegers/RTL8188-hostapd/archive/v1.1.tar.gz
echo ""
echo "Unpacking...."
echo ""
tar -zxvf v1.1.tar.gz
echo ""
echo "Moving into \"RTL8188-hostapd-1.1/hostapd/\""
echo ""
cd RTL8188-hostapd-1.1/hostapd
echo ""
echo "Running make..."
echo ""
sudo make
echo ""
echo "Running install...."
echo ""
sudo make install

cd ../../
echo ""
echo "Configuring dhcp..."
echo ""
cd dhcp/
sudo cp dhcpd.conf /etc/dhcp/
cd ../
#sudo nano /etc/dhcp/dhcpd.conf
#   Coment thease out
#option domain-name "example.org";
#option domain-name-servers ns1.example.org, ns2.example.org;

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.
#authoritative; <--- remove

#   Add the following
#subnet 192.168.10.0 netmask 255.255.255.0 {
# range 192.168.10.10 192.168.10.20;
# option broadcast-address 192.168.10.255;
# option routers 192.168.10.1;
# default-lease-time 600;
# max-lease-time 7200;
# option domain-name "local-network";
# option domain-name-servers 8.8.8.8, 8.8.4.4;
#}

cd dhcp-server/
sudo cp isc-dhcp-server /etc/default/
cd ../
#sudo nano /etc/default/isc-dhcp-server
#   Update to this
#INTERFACES="wlan0"


echo ""
echo "Shutting down wlan0..."
echo ""
sudo ifdown wlan0
echo ""
echo "Editing \"/etc/network/interfaces\""
echo ""
cd interface_one/
sudo cp interfaces /etc/network/
cd ../

#sudo nano /etc/network/interfaces
#   add this
#allow-hotplug wlan0
#iface wlan0 inet static
# address 192.168.10.1
# netmask 255.255.255.0
#hashtag out last 3 lines

echo ""
echo "Editing hostapd configuration..."
echo ""
cd hostapd/
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
cd ../

#sudo nano /etc/hostapd/hostapd.conf
#The standard configuration will create a new wireless network 
#called wifi with the password YourPassPhrase. You can change the parameter
# “ssid=wifi” to the SSID wifi name you want and the parameter
 # “wpa_passphrase=YourPassPhrase” to your own password.

echo ""
echo "Adding sysctl configuration.."
echo ""
cd sysctl/
sudo cp sysctl.conf /etc/
cd ../
#sudo nano /etc/sysctl.conf
 #add this at bottom
 #net.ipv4.ip_forward=1

sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

echo ""
echo "Starting wlan0..."
echo ""
sudo ifup wlan0

echo ""
echo "Setting up iptables..."
echo ""
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

echo ""
echo "Starting services..."
echo ""
sudo service isc-dhcp-server start
sudo service hostapd start
echo ""
echo "Enabling services..."
echo ""
sudo update-rc.d hostapd defaults
sudo update-rc.d isc-dhcp-server enable
sudo update-rc.d hostapd enable 


echo ""
echo "Saving ipdatbles..."
echo ""
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

#   add to /etc/network/interfaces
#up iptables-restore < /etc/iptables.ipv4.nat
echo ""
echo "Editing interfaces..."
echo ""
cd interface_two/
sudo cp interfaces /etc/network/

echo ""
echo "Brace for reboot..."
echo ""
sudo reboot
