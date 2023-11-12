from machine import Pin,PWM
from time import sleep
freq = 50
Servo = PWM(Pin(5), freq)
while True:
    for i in range(115,40,-1):
        Servo.duty(i)
        sleep(0.05)
    for i in range(41,115,1):
        Servo.duty(i)
        sleep(0.05)
