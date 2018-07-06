#!/bin/bash

DEVICEID=$1
FILE=config.yaml

perl -pi -e "s/^  device_connection_string: \"\"/  device_connection_string: \"$DEVICEID\"/g" $FILE

exit

sudo apt-get update

sudo apt-get install moby-engine
sudo apt-get install moby-cli 

sudo apt-get update
sudo apt-get install iotedge


# edit /etc/iotedge/config.yaml



sudo systemctl restart iotedge
sudo systemctl status iotedge
