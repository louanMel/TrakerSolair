from machine import Pin, PWM
import time

def set_angle(servo_pwm, angle):
    print('func')
    duty = int(-35*angle+8000)
    print('duty')
    servo_pwm.duty_u16(duty)
    print('func fini')

servo_pin = Pin(15)
servo_pwm = PWM(servo_pin)


servo_pwm.freq(50)
print('freq')

set_angle(servo_pwm, 0)
time.sleep(0.5)
print('fini1')
set_angle(servo_pwm, 20)
time.sleep(0.5)
print('fini2')
set_angle(servo_pwm, 10)
time.sleep(0.5)
print('fini3')

print('fini')
