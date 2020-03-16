import RPi.GPIO as GPIO
import time
import random

led_1 = 40
led_2 = 33
led_3 = 35
led_4 = 37


GPIO.setwarnings(False) #to desable the warning
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_1, GPIO.OUT)
# GPIO.setup(led_2, GPIO.OUT)
# GPIO.setup(led_3, GPIO.OUT)
# GPIO.setup(led_4, GPIO.OUT)
GPIO.output(led_1,GPIO.HIGH)
time.sleep(2)
GPIO.output(led_1,GPIO.LOW)




#for i in range(10):
#     time.sleep(.05)
#     GPIO.output(led_2,GPIO.HIGH)
#     

GPIO.cleanup() #this is for cleanup the all gpio
print("clean")