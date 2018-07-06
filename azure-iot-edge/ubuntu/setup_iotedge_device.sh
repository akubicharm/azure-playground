#!/bin/bash

DEVICEID=$1
FILE=/etc/iotedge/config.yaml


# prepare

prep_package() {
  curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > ./microsoft-prod.list
  cp ./microsoft-prod.list /etc/apt/sources.list.d/

  curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
  cp ./microsoft.gpg /etc/apt/trusted.gpg.d/
}




install_package() {
  apt-get update

  apt-get install moby-engine
  apt-get install moby-cli 

  apt-get update
  apt-get install iotedge
}




config_iotedge() {
  # edit /etc/iotedge/config.yaml
  perl -pi -e "s/^  device_connection_string: \"\"/  device_connection_string: \"$DEVICEID\"/g" $FILE
}



start_iotedge() {
  systemctl restart iotedge
  systemctl status iotedge
}


prep_package
install_package
config_iotege
start_iotedge
