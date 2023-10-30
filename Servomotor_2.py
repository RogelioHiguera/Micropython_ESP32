from machine import Pin, ADC, PWM
from time import sleep
freq = 50
Servo = PWM(Pin(5), freq)
Pot = ADC(Pin(34))
Pot.atten(ADC.ATTN_11DB)
Pot.width(ADC.WIDTH_9BIT)
while True:
    #duty de 40 a 115
    Servo.duty(Pot.read())
    sleep(0.01)