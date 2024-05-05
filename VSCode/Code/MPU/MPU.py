import board
import busio
import time
import math
from MPU.mpu9250 import MPU9250
from MPU.mpu6500 import MPU6500
from MPU.ak8963 import AK8963


class MPU:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.mpu = MPU6500(self.i2c, address=0x68)      
        self.ak = AK8963(self.i2c)
        self.sensor = MPU9250(self.mpu, self.ak)
        
        self.impact = 0.0
        self.lastTime = time.monotonic()
        
        self.bufferLenght = int (2)
        self.buffer = [0] * self.bufferLenght

        print("Reading in data from IMU.")
        print("MPU9250 id: " + hex(self.sensor.read_whoami()))

    def debugPrintData(self):
        print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*self.sensor.read_acceleration()))
        print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*self.sensor.read_magnetic()))
        print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*self.sensor.read_gyro()))
        print('Temperature: {0:0.3f}C'.format(self.sensor.read_temperature()))
        
    def GetSample(self):
        sample = self.sensor.read_gyro()
        return sample[0] ** 2 + sample[1] ** 2 + sample[2] ** 2
    
    def Update(self):
        currenTime = time.monotonic()
        delta = currenTime - self.lastTime
        self.lastTime = currenTime
        length = self.GetSample()
        length *= delta
        self.buffer.pop(0)
        self.buffer.append(length)
        
        self.impact = 0
        for i in range(self.bufferLenght):
            self.impact += self.buffer[i]
        
        self.impact /= self.bufferLenght
        
    def DetectImpact(self):
        return self.impact > 50 