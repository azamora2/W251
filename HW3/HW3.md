# Homework 3 by Andres Zamora, instructions to run

## look at my S3 bucket

- https://s3.us-south.cloud-object-storage.appdomain.cloud/cloud-object-storage-andres-e-zamora-bh-cos-standard-2qv/

## First create the bridge alpine container and the forwarding alpine container connected to the same network locally in the TW-2

```
# Create a bridge:
docker network create --driver bridge hw03
# Create an alpine linux - based mosquitto container:
docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh
# we are inside the container now
# install mosquitto
apk update && apk add mosquitto
# run mosquitto
/usr/sbin/mosquitto
# Press Control-P Control-Q to disconnect from the container

# Create an alpine linux - based message forwarder container:
docker run --name forwarder --network hw03 -ti alpine sh
# we are inside the container now
# install mosquitto-clients
apk update && apk add mosquitto-clients
ping mosquitto
# this should work - note that we are referring to the mosquitto container by name
mosquitto_sub -h mosquitto -t <some topic>
# the above should block until some messages arrive
# Press Control-P Control-Q to disconnect from the container
```
- place the `forwader.py` file in the forwarder container
## Build the CUDA_dockerfile and run it

 - Build the CUDA_Dockerfile

```
docker build -t CUDA_container -f CUDA_Dockerfile .
```
 - Run he CUDA_Dockerfile attached to a container

```
docker run -e DISPLAY=$DISPLAY --privileged --network hw03 --env QT_X11_NO_MITSHM=1 --name CUDA_container_bash --rm -i -t CUDA_container
```

## Install VIM, PIP, and numpy in the CUDA container

- Install VIM, PIP, and numpy in the CUDA container

```
apt-get install VIM
apt-get install python-pip
pip install numpy
```

## Create a bridge container in the VM instance

```
# Create a bridge:
docker network create --driver bridge hw03
# Create an alpine linux - based mosquitto container:
docker run --name mosquitto2 --network hw03 -p 1883:1883 -ti alpine sh
# we are inside the container now
# install mosquitto
apk update && apk add mosquitto
# run mosquitto
/usr/sbin/mosquitto
# Press Control-P Control-Q to disconnect from the container
```
## Build an ubuntu container to save the images in the S3 bucket
- place the `saver_dockerfile` file in the VM instance
-redirect the `broker` variable in the `forwarder.py` file to the public ip address of the VM instance
-build the Ubuntu container
```
docker build -t saver_container -f saver_dockerfile .
```
- Mount the S3 bucket in the VM instance using the following command:

```
s3fs MYBUCKET /mnt/mybucket -o passwd_file=$HOME/.cos_creds -o use_path_request_style -o url=https://s3.us-east.cloud-object-storage.appdomain.cloud
```
## Run the Ubuntu container and the save images to the cloud
- Run the Ubuntu container

```
docker run -e DISPLAY=$DISPLAY --privileged --network hw03 -v /mnt/mybucket:/data --name saver_bash --rm -i -t saver_container
```
- Install VIM, PIP, and numpy in the Ubuntu container

```
apt-get install VIM
apt-get install python-pip
pip install numpy
```
- place the `saver.py` file in the Ubuntu container
- Run the `saver.py` file in the Ubuntu container
- Run the `forwarder.py` file in the Alpine forwarder container
- Run the `image_taker.py` file in the CUDA container
