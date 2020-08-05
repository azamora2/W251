# Final project
The motivation behind this project was to build a face mask detection model that would detect if you were not wearing a mask and send over thos images to cloud storage so that a company that is potentially interested can detect whether certain employees or customers are not wearing their facemasks and keep a record of this. my images are here: https://s3.us-south.cloud-object-storage.appdomain.cloud/andres-cos-standard-api/
## instructions for running the face mask detector
- If you want to create your own dataset dowload your own set of images with the `download_faces.sh` script in this file
- Afterwads you can label half of them by putting the png of a facemask on top of it using picmonkey.com

## To Run the code once you have the data
- First you need to run the training in a v100 vsi with flavor AC2_8X60X10

```
ibmcloud sl vs create --datacenter=dal12 --hostname=v100 --domain=dima.com --image=2263543 --billing=hourly --network 1000 --key=1831742 --flavor AC2_8X60X100 --san
```
- Then you need to pull the following docker container an upload the dataset, the fasmask_detector folder and thetrain_facemask_model.ipynb o the jupyter container uploading a zip file and then unzipping it is the fastest way to do it

```
docker pull jupyter/tensorflow-notebook
docker run -p 8888:8888 jupyter/tensorflow-notebook
```
- Afterwards make sure you run the train_facemask_model.ipynb with the appropirate cells to install and import opencv and imutils

- Train the model, and download the facemask_detector.model to your computer

- set up alpine bridge containers in your TX2 and in the your VSI just like for HW3 and HW7 explained in this repository

- pull the tensorrt docker container and run it like in week 05 and upload the image_taker.ipynb jupyter notebook

- set up the object storage 
follow the instructions for the class and in the end to mount it run the following command: 
```
sudo s3fs andres-cos-standard-api /mnt/mybucket  -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us-south.objectstorage.softlayer.net

```
where `andres-cos-standard-api` is the name of the bucket
```
sudo s3fs andres-cos-standard-api /mnt/mybucket  -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us-south.objectstorage.softlayer.net
```
also make sure you are using the correct url whether it is us-south or us-north

- set up the alpine container in your VSI and the run_facemask_files_here.ipynb notebook will take care of saving the images
pull the following docker container to run the image detection jupyter notebook 
```
docker pull  tensorflow/tensorflow:nightly-jupyter
docker run --network hw03 --privileged --rm -it --user root -v /mnt/mybucket:/tf/work -p 8888:8888 tensorflow/tensorflow:nightly-jupyter
```
- upload the facemask_detector folder the examples folder the detect_facemask_in_realtime.py and the detect_facemask_indicidual_image.py and run_facemask_files_here.ipynb to the tensorflow/tensorflow:nightly-jupyter container

run the .py files in the `run_facemask_files_here.ipynb`

- set up the bridge alpine container in the TX2 and upload and run the forwarder.py program inside it afer installing vim and paho mqtt and pip etc.

- after setting up the alpine bride network and containers in the TX2 like in homework 3 pulling the  tensorrt container from lab week05 and uploading the image_taker.ipynb. Run the cells in image_taker.ipynb 

this should cause the images to detect faces in real time and if you are not wearing a mask send those files to the cloud storage

in this case here:
https://s3.us-south.cloud-object-storage.appdomain.cloud/andres-cos-standard-api/


- invariably if you only wish to see if the model can detect certain images place them in the examples folder and run the  `run_facemask_files_here.ipynb` cells after you have tweeked line 13 of `detect_facemask_individual_image.py` with the path and name of the image you want to evaluate

```
image_path = "/tf/face-mask-detector4/examples/Con_cubrebocas.jpg"
```
and line  line 83 of `detect_facemask_individual_image.py`  if you want the evaluated image to have a certain name or be placed in a certain path

```
cv2.imwrite("/tf/face-mask-detector4/facemask_detection_output.jpg", image)
```

thank you

The results after this endevour were the files in te object storage: https://s3.us-south.cloud-object-storage.appdomain.cloud/andres-cos-standard-api/

and the following after trainig as well as some evaluated images below (cubrebocas is face mask in spanish and sin cubre bocas is no facemask p.s. sorry I forgot to change it) bellow is also the evaluation of the trained head network build on top of a face regognition imagenet V2 model:
```
-------------EVALUATING HEAD NETWORK----------------
              precision    recall  f1-score   support
   with_mask       1.00      1.00      1.00       138
without_mask       1.00      1.00      1.00       138
    accuracy                           1.00       276
   macro avg       1.00      1.00      1.00       276
weighted avg       1.00      1.00      1.00       276
--------------------SAVING MODEL---------------------
```
![Alt text](https://github.com/azamora2/W251/blob/master/FinalProject/plot.png "accuracy and loss graph")
![Alt text](https://github.com/azamora2/W251/blob/master/FinalProject/carmen.jpg "carmen")
![Alt text](https://github.com/azamora2/W251/blob/master/FinalProject/andres_cubrebocas.jpg "Facemask")
![Alt text](https://github.com/azamora2/W251/blob/master/FinalProject/andres_sin_cubrebocas.jpg "No facemask")
