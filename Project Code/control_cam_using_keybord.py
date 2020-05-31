from tkinter import *  #keyboard imput library
from picamera import PiCamera # import picamera library
from time import sleep #import sleep form time library

camera = PiCamera() # create object for camera
root = Tk()  #crete object for keybord input

def capture_image():
    sleep(2)
    camera.capture('/home/pi/Desktop/image4.jpg')
    




