# Programme permettant la gestion d'un servomoteur

# from machine import Pin,PWM

def initservo(servo,angle):
    servo.freq(50)
    position(servo,angle)          # Fonction d'initialisation du servomoteur

def position(servo,angle):         # Fonction permettant de positionner le servomoteur
    temps_haut = -35*angle+8000
    servo.duty_u16(temps_haut) 