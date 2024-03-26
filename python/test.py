from machine import Pin, PWM
from servomoteur import *
import time

servo_v = PWM(Pin(15))
initservo(servo_v, 0)
servo_h = PWM(Pin(25))
initservo(servo_h, 0)


for angle in range(10, 50, 1):
    angle_h = angle
    angle_v = angle*2
    position(servo_h, angle_h)
    position(servo_v, angle_v)
    print("Angle:", angle)
    time.sleep(0.5)