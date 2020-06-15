import numpy as np
import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto2"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test_topic"


count = 0
def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
  try:
    print("message received!")
    global count
    count = count+1
    print(count)
    # if we wanted to re-publish this message, something like this should work
    message = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    with open('/data/test'+str(count)+'.bin','wb') as f:
         f.write(message)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message
local_mqttclient.subscribe(LOCAL_MQTT_TOPIC)
local_mqttclient.loop_forever()

