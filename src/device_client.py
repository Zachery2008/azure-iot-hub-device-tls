# Reference: 
# https://techcommunity.microsoft.com/t5/internet-of-things-blog/azure-iot-tls-critical-changes-are-almost-here-and-why-you/ba-p/2393169#:~:text=The%20time%20has%20come%20now,does%20not%20impact%20sovereign%20clouds.
# https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support

from paho.mqtt import client as mqtt
import ssl

#PATH_TO_ROOT_CERT = "./certs/BaltimoreCyberTrustRoot.crt"
PATH_TO_ROOT_CERT = "./certs/DigiCertGlobalRootG2.crt.pem"
DEVICE_ID = "TestDevice1"
SAS_TOKEN = "iNULmN6ja++HvY6wXvYW9RQyby0nQYZB+0IUiUPpfec="
IOT_HUB_NAME = "g2cert"


def on_connect(client, userdata, flags, rc):
  print("Device connected with result code: " + str(rc))


def on_disconnect(client, userdata, rc):
  print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
  print("Device sent message")


client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.username_pw_set(username=IOT_HUB_NAME+".azure-devices.net/" + DEVICE_ID + "/?api-version=2021-04-12", password=SAS_TOKEN)

client.tls_set(ca_certs=PATH_TO_ROOT_CERT, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(False)

client.connect(IOT_HUB_NAME+".azure-devices.net", port=8883)

client.publish("devices/" + DEVICE_ID + "/messages/events/", '{"id":123}', qos=1)
client.loop_forever()