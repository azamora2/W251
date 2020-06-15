import numpy as np
import cv2
import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
  try:
    print("message received!")
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)
count = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = cv2.imwrite("frame.png", frame)
    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    #gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    print(face_cascade.load('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'))
    # gray here is the gray frame you will be getting from a camera
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if np.any(faces):
        for (x,y,w,h) in faces:
            # your logic goes here; for instance
            # cut out face from the frame..
            #pt1 = (int(x), int(y))
            #pt2 = (int((x + w)), int((y + h)))
            face_region = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
            sub_face = gray[y:y+h, x:x+w]
            #roi_gray = gray[y:y+h, x:x+w]
            # rc,png = cv2.imencode('.png', face)
            # msg = png.tobytes()
            if np.any(face_region):
                #count = count +1
                #local_mqttclient.publish(LOCAL_MQTT_TOPIC,payload='Cara de Andres/Andres face '+str(count))
		rc,png = cv2.imencode('.png', sub_face)

                msg = png.tobytes()

                local_mqttclient.publish(LOCAL_MQTT_TOPIC,payload=msg)
                #print('yes '+str(count))
                #cv2.imshow('cnts',sub_face)
                #cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()


