# ------------------------------ 
# Python 2.7.x required
# 
#
# ------------------------------ 

from base64 import b64encode, b64decode
from hashlib import sha256
from time import time
from urllib import quote_plus, urlencode
from hmac import HMAC
import requests
from paho.mqtt import client as mqtt
import ssl


#
# Generate SAS Token
# Parameters:
#   uri: IoT Hub URI(CName)
#   key: IoT Hub Shared access key or Device key
#   policy_name: IoT Hub shared access policy
#   expiry: expiry seconds
#
def generate_sas_token(uri, key, policy_name, expiry=3600):
    ttl = time() + expiry
    sign_key = "%s\n%d" % ((quote_plus(uri)), int(ttl))
    signature = b64encode(HMAC(b64decode(key), sign_key, sha256).digest())

    rawtoken = {
        'sr' : uri,
        'sig': signature,
        'se' : str(int(ttl))
    }

    if policy_name is not None:
        rawtoken['skn'] = policy_name

    return 'SharedAccessSignature ' + urlencode(rawtoken)



#
# VARAIBLES
#
path_to_root_cert = "local_root_ca.cer"
iot_hub_name = "<REPLACE YOUR IOT HUB NAME>
iot_hub_cname = iot_hub_name + ".azure-devices.net"
device_id = "<REPLACE YOUR DEVICE ID>"


# Use IoT Hub Shared Access Key
iot_hub_device_connect_key = "<REPLACE IOT HUB SHARED CONNECT KEY>
sas_token = generate_sas_token(iot_hub_cname, iot_hub_device_connect_key, "device")

# Use IoT Device Shared Access key
#iot_device_connect_key = "<REPLACE YOUR DEVICE KEY>"
#sas_token = generate_sas_token(iot_hub_cname, iot_device_connect_key, None)


#
# FUNCTIONS
#
def on_connect(client, userdata, flags, rc):
  print ("Device connected with result code: " + str(rc))
def on_disconnect(client, userdata, rc):
  print ("Device disconnected with result code: " + str(rc))
def on_publish(client, userdata, mid):
  print ("Device sent message")


#
# MAIN
#
client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.username_pw_set(username=iot_hub_name+".azure-devices.net/" + device_id, password=sas_token)

client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
client.tls_insecure_set(False)

client.connect(iot_hub_name+".azure-devices.net", port=8883)

client.publish("devices/" + device_id + "/messages/events/", "{id: 123}", qos=1)
client.loop_forever()
