import RPi.GPIO as GPIO
import time

led_1 = 40

GPIO.setwarnings(False) #to desable the warning
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_1, GPIO.OUT)

for i in range(0,2):
        
    GPIO.output(led_1,GPIO.HIGH)
    time.sleep(.3)
    GPIO.output(led_1,GPIO.LOW)
    time.sleep(.3)
    GPIO.output(led_1,GPIO.HIGH)
    time.sleep(.3)
    GPIO.output(led_1,GPIO.LOW)
    time.sleep(.3)
    GPIO.output(led_1,GPIO.HIGH)
    time.sleep(.3)
    GPIO.output(led_1,GPIO.LOW)
    time.sleep(.3)

GPIO.cleanup() #this is for cleanup the all gpio


