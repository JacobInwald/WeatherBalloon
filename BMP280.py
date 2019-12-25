
import time
import board
import busio
import adafruit_bmp280

class pressure_sensor:
'''
provides pressure(hPa) and backups for temperature(C) and altitude(m)
'''
    i2c = busio.I2C(board.SCL, board.SDA)
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
    ground_pressure = bmp280.sea_level_pressure 

    def __init__(self, ground_pressure):
        self.ground_pressure = ground_pressure

    def pressure(self):
        return self.pmp280.pressure

    def temperature(self):
        return self.bmp280.temperature

    def altitude(self):
        return self.bmp280.altitude
    
 
