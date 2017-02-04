#!/bin/bash

# -a makes read read into a array. fyi for further dev.
echo "Injecttion script to publish to local mqtt broker. you are publishing from $HOSTNAME"
echo "Please write what line you want to edit:"
echo -n ">"
read word
echo "Please write a value you want to insert into that line:"
echo -n ">"
read word2
sudo mosquitto_pub -t SPARC/home_automation/config -m "{\"$word\":\"$word2\"}"
echo "Injected \"$word:$word2\" into SPARC/home_automation/config"
