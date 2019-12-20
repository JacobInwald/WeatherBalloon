# WeatherBalloon
JCosmos Weather Balloon Sensor Project

## Project Setup
<a>This project consists of multiple parts. These include the different sensors and hardware. </a> \n
<a>This readme should detail how to setup this project. </a>
The different parts are as follows:
* Main.py (This is the place where all the sensor code is implemented)
* HumiditySensor.py (This is the humidity sensor code)

### Humidity Sensor

This sensor code requires some setup before it works.

#### Dependencies
- python-dev and python-openssl
- github repo Adafruit_DHT

#### Setup Code

- First run the commands: `sudo apt-get update` and then `sudo apt-get install build-essential python-dev python-openssl git`. What this will do is just install python-dev and python-openssl.
- Then run the commands: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT` and then `sudo python setup.py install`. This will download the git repo Adafruit_DHT and then set it up.

Now the Humidity Sensor should be set up!
