#!/bin/bash
HUBNAME=$1
DEVNAME=$2


echo "az iot device create --hub-name $HUBNAME --device-id $DEVNAME"
az iot device create --hub-name $HUBNAME --device-id $DEVNAME
