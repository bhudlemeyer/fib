# Brandon Fibonacci project

## Running locally with python

Clone this github repository to your machine, and ensure you have python version 3 or above installed.
 Then run the following command from inside the project directory to install required python packages.
```
pip3 install -r requirements.txt

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

run following command from within the project directory to build the docker image
```
sudo docker build -t NAME_YOU_WANT_FOR_IMAGE --build-arg PORT=PORT_YOU_WANT_APP_TO_LISTEN_ON .

```
If you do not add the --build-arg PORT= the port will default to 8080.

### run the following command to start the newly created docker image on your local machine

```
sudo docker run -d --name NAME_YOU_WANT_FOR_CONTAINER -p localport:PORT_YOU_CONFIGURED_IN_BUILD_PROCESS IMAGENAME
```

## Using the app

To access the app no matter which way you brought it up simply navigate to the following url

```
http://hostip:port/
```

This will drop you at the welcome screen with usage information for the app it self.


To go directly to the api endpoint simply curl or open the following endpoint in a browser

```
http://hostip:port/v1/fib/(Positive_Number)

for example

curl http://10.0.5.11:8081/v1/fib/5
returns
[0, 1, 1, 2, 3, 5]
```


# Perform unit tests

To perform unit testing of the app in a seperate window start the app via the python3 method listed above.

Once the app is running from the root of the project directory simply run

```
python3 test/test_basic.py
```

