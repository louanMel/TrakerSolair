from machine import Pin, PWM
import time

# Initialise le servo sur la broche D2
servo_pin = Pin(3)
servo_pwm = PWM(servo_pin)

# Définit la fréquence du PWM à 50 Hz (standard pour les servomoteurs)
servo_pwm.freq(50)

# Fonction pour définir l'angle du servo
def set_angle(angle):
    # Convertit l'angle en valeur de rapport cyclique PWM
    duty = int((angle / 180) * 1023 + 128)
    servo_pwm.duty_u16(duty)

# Définit la position du servo à 5, 10, puis 15 degrés avec des pauses de 2 secondes entre chaque mouvement
set_angle(5)
print('turn1')
time.sleep(2.0)
set_angle(30)
print('turn2')


