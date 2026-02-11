import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 0
button = 6
GPIO.setup(button, GPIO.IN)
while True:
    if GPIO.input(button): 
        state = 0   
        GPIO.output(led, state)
        time.sleep(0.2)
    else:
        state=1
        GPIO.output(led, state)
        time.sleep(0.2)
        