# docker pull jupyter/tensorflow-notebook
# docker run -p 8888:8888 jupyter/tensorflow-notebook
# python detect_mask_image.py --image examples/example_01.png

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os

image_path = "/tf/face-mask-detector4/examples/Con_cubrebocas.jpg"
facedetector_path = '/tf/face-mask-detector4/face_detector/'
model_path = "/tf/face-mask-detector4/face_detector/facemask_detector.model"
confidence_threshold = 0.7

# load serialized face detector model
print("------------------LOADING FACE DETECTOR MODEL------------------------")
prototxt = os.path.sep.join([facedetector_path, "deploy.prototxt"])
face_weights = os.path.sep.join([facedetector_path,
	"res10_300x300_ssd_iter_140000.caffemodel"])
image_net = cv2.dnn.readNet(prototxt, face_weights)

# load face mask detector model
print("----------------LOADING FACE MASK DETECTOR MODEL---------------------")
model = load_model(model_path)

# load the input image, copy it, and grab its width and height
image = cv2.imread(image_path)
original_image = image.copy()
(height, width) = image.shape[:2]

# make a blob from image
blob_image = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
	(104.0, 177.0, 123.0))

# pass blob through the network and obtain face detections
print("---------------COMPUTING FACE MASK DETECTIONS------------------------")
print(confidence_threshold)
image_net.setInput(blob_image)
face_detections = image_net.forward()

# loop over detections
for i in range(0, face_detections.shape[2]):
	# extract the confidence/probability associated with detection
	confprob = face_detections[0, 0, i, 2]

	# get rid of weak detections ensuring the confidence is greater than the confidence threshold
	if confprob > confidence_threshold:
		# compute the (x, y)-coordinates of the bounding box for the detection
		box = face_detections[0, 0, i, 3:7] * np.array([width, height, width, height])
		(Xstart, Ystart, Xfin, Yfin) = box.astype("int")

		# make sure the bounding boxes fall within frame dimensions
		(Xstart, Ystart) = (max(0, Xstart), max(0, Ystart))
		(Xfin, Yfin) = (min(width - 1, Xfin), min(height - 1, Yfin))
		print('hello')        
		face = image[Ystart:Yfin, Xstart:Xfin] # extract face ROI 
		face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB) #convert BGR to RGB
		face = cv2.resize(face, (224, 224)) #resize detection to 224x224
		face = img_to_array(face) #preprocess
		face = preprocess_input(face) #preprocess
		face = np.expand_dims(face, axis=0) #preprocess
		print('hello') 
		# pass the face through the model to detect face mask or not
		(mask, withoutMask) = model.predict(face)[0]
		print('hello') 
		# decide class label and make green bounding box and label if there is face mask otherwise red
		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

		# Make the probability appear in the label
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		# display the label and bounding box on the image
		cv2.putText(image, label, (Xstart, Ystart - 10),
			cv2.FONT_HERSHEY_DUPLEX, 0.75, color, 2)
		cv2.rectangle(image, (Xstart, Ystart), (Xfin, Yfin), color, 2)

# save output image
#cv2.imshow("Output", image)
cv2.imwrite("/tf/face-mask-detector4/facemask_detection_output.jpg", image)
print('hola')
cv2.waitKey(0)
