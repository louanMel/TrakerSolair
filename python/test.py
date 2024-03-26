from machine import Pin, PWM
from servomoteur import *
import time

servo_v = PWM(Pin(15))
initservo(servo_v, 0)
servo_h = PWM(Pin(25))
initservo(servo_h, 0)


for angle in range(10, 150, 1):  # Test de chaque angle
    position(servo_h, angle)
    position(servo_v, angle)
    print("Angle:", angle)
    time.sleep(0.5)