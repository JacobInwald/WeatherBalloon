
import time
import board
import busio
import adafruit_bmp280

class pressure_sensor:
    
'''
provides pressure(hPa) and backups for temperature(C) and altitude(m)
'''
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
        '''
            creating ground readings of basic data for later comparison
        '''
        self.pressureList = []
        self.altitudeList = []
        self.temperatureList = []
        self.pressureList.append(self.getPressure)
        self.altitudeList.append(self.getAltitude)
        self.temperatureList.append(self.getTemperature)

    def getPressure(self):
        return self.bmp280.pressure

    def getTemperature(self):
        return self.bmp280.temperature

    def getAltitude(self):
        return self.bmp280.altitude
    
    def tick(self):
        '''
            to be run continuously to get updates throughout flight
        '''
        self.pressureList.append(self.get_pressure())
        self.altitudeList.append(self.get_altitude())
        self.temperatureList.append(self.get_append())
