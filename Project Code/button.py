from gpiozero import  Button
from time import sleep

button = Button(3)

while True:
    if button.wait_for_press():
        print("button pressed")

    