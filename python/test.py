import time
from servo import Servo

my_servo = Servo(pin_id=3)
my_servo.write(5)
time.sleep(2.0)
my_servo.write(10)
time.sleep(2.0)
my_servo.write(15)