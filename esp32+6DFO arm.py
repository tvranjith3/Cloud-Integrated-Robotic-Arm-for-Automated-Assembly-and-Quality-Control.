from machine import I2C, Pin
import pca9685
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
pwm = pca9685.PCA9685(i2c)
pwm.freq(50)

def set_servo(channel, angle):

    pulse = int(150 + (angle/180)*450)
    pwm.duty(channel, pulse)

while True:

    # Base
    set_servo(0, 90)

    # Shoulder
    set_servo(1, 60)

    # Elbow
    set_servo(2, 100)

    time.sleep(2)

    # Close gripper
    set_servo(5, 30)

    time.sleep(2)

    # Move to drop zone
    set_servo(0, 120)

    time.sleep(2)

    # Open gripper
    set_servo(5, 90)

    time.sleep(4)