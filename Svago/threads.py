from paho.mqtt import client
from paho.mqtt.client import Client

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK Returned code=",rc)
        #client.subscribe(topic)
    else:
        print("Bad connection Returned code= ",rc)

client = Client('1')

client.connect('mqtt.eclipse.org', 1883)

client.loop_read()