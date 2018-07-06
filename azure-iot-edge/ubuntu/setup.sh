#!/bin/bash

DEVICEID=$1
FILE=/etc/iotedge/config.yaml

perl -pi -e "s/^  device_connection_string: \"\"/  device_connection_string: \"$DEVICEID\"/g" $FILE

exit

apt-get update

apt-get install moby-engine
apt-get install moby-cli 

apt-get update
apt-get install iotedge


# edit /etc/iotedge/config.yaml



systemctl restart iotedge
systemctl status iotedge
