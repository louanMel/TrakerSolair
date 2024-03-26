from machine import Pin, PWM
from servomoteur import *
import time

servo_h = PWM(Pin(25))
initservo(servo_h, 0)
servo_v = PWM(Pin(15))
initservo(servo_v, 0)


position(servo_h, 45)
position(servo_v, 45)