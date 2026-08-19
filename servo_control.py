from machine import Pin, PWM
from time import sleep

# Servo signal pin
servo = PWM(Pin(3))
servo.freq(50)

def set_angle(angle):
    min_duty = 26
    max_duty = 128

    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty(duty)
    sleep(1)


# Test servo movement
while True:
    set_angle(0)
    sleep(2)

    set_angle(90)
    sleep(2)

    set_angle(180)
    sleep(2)
