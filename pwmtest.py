import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin=18
GPIO.setup(pin, GPIO.OUT)
pwm=GPIO.PWM(pin, 50)
duty=10
pwm.start(duty)
time.sleep(1)
pwm.ChangeDutyCycle(5)
time.sleep(1)
