# Brandon Fibonacci project

## Running locally with python

Clone this github repository to your machine, and ensure you have python version 3 or above installed.
 Then run the following command from inside the git directory to install required python packages.
```
pip3* install -r requirements.txt

``` 
*for purposes of this readme it will be assumed you need to add 3 to the end of python and pip commands to utilize pythonv3*

### run the following command to start the application locally

```
python3 app/main.py

```
This will bring the app up listening on all interfaces on port 8080

## Setup with Docker
Clone the github repository to your machine
ensure docker is installed and running on your machine

run following command to build the docker image
```
sudo docker build -t NAME_YOU_WANT_FOR_IMAGE --build-arg port=PORT_YOU_WANT_APP_TO_LISTEN_ON

```
If you do not add the --build-arg port= the port will default to 8080.



