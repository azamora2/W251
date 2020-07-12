# Homework 3 by Andres Zamora, instructions to run

## look at my S3 bucket
- https://andresito-cos-standard-x95.s3.us-south.cloud-object-storage.appdomain.cloud/
- Mount everything just like for homework3 but be mindful of assigning the right Us location when doing the final mount command
- The files that changed from homework 3 to homework 7 are the input notebook file and the saver.py file both attached in this folder
### Questions
* Describe your solution in detail.  What neural network did you use? What dataset was it trained on? What accuracy does it achieve?
A mobilenet SSD(single shot multibox detector) based face detector with pretrained model provided, powered by tensorflow object detection api, trained by WIDERFACE dataset.It achieves 99% accuracy.
* Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?
Yes it achieves very good accuracy. I would use this solution to develop a production rate system if the frame rate was not an issue
* What framerate does this method achieve on the Jetson? Where is the bottleneck? 
One frame per second. The bottleneck occurs when opening the image path to read the image
* Which is a better quality detector: the OpenCV or yours? 
OpenCV has a faster frame rate but mine seems to have better accuracy.

- instructions Mount the S3 bucket in the VM instance using the following command (Make sure you get the correct area in the US):

```
s3fs MYBUCKET /mnt/mybucket -o passwd_file=$HOME/.cos_creds -o use_path_request_style -o url=https://s3.us-south.cloud-object-storage.appdomain.cloud
```
