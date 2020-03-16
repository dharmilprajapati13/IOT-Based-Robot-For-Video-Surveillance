import RPi.GPIO as GPIO
import time
from tkinter import *

has_prev_key_release = None



root = Tk() #making object for TK small display comes because of it
root.title('take input form keybord')


#set pin for motor A left side of the l298
en_a = 33
in_1 = 35
in_2 = 37

#set pin for motor B right side of the l298
en_b = 36
in_3 = 38 
in_4 = 40

GPIO.setwarnings(False) #to desable the warning

# initial_speed = 90




#setup function to set the all gpio pins 
def setup():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(en_a, GPIO.OUT)
    GPIO.setup(in_1, GPIO.OUT)
    GPIO.setup(in_2, GPIO.OUT)
    
    GPIO.setup(en_b, GPIO.OUT)
    GPIO.setup(in_3, GPIO.OUT)
    GPIO.setup(in_4, GPIO.OUT)
    
    
    #speed_a = GPIO.PWM(en_a,100)
    #speed_b = GPIO.PWM(en_b,100)

    #speed_a.start(initial_speed)
    #speed_b.start(initial_speed)
    
#function for forword move
#en_a = 1, in_1 = 1, in_2 = 0 for motor A
#en_b = 1, in_3 = 1, in_4 = 0 for motor B
#both moter will move forword direction
def forword():

    setup()
    #for motor A 
    GPIO.output(en_a,GPIO.HIGH)
    GPIO.output(in_1,GPIO.HIGH)
    GPIO.output(in_2,GPIO.LOW)
    print("forword")
    
    #for motor B 
    GPIO.output(en_b,GPIO.HIGH)
    GPIO.output(in_3,GPIO.HIGH)
    GPIO.output(in_4,GPIO.LOW)
    


#function for backword move
#en_a = 1, in_1 = 0, in_2 = 1 for motor A
#en_b = 1, in_3 = 0, in_4 = 1 for motor B
#both moter will move backword direction
def backword():

    setup()
    #for motor A 
    GPIO.output(en_a,GPIO.HIGH)
    GPIO.output(in_1,GPIO.LOW)
    GPIO.output(in_2,GPIO.HIGH)
    print("backword")

    
    #for motor B 
    GPIO.output(en_b,GPIO.HIGH)
    GPIO.output(in_3,GPIO.LOW)
    GPIO.output(in_4,GPIO.HIGH)
    

    
#function for right turn
#en_a = 1, in_1 = 1, in_2 = 0 for motor A
#en_b = 1, in_3 = 0, in_4 = 0 for motor B
#left motor (A) will move forword and right motor (B) will remain stop
def right_turn():

    setup()
    #for motor A 
    GPIO.output(en_a,GPIO.HIGH)
    GPIO.output(in_1,GPIO.HIGH)
    GPIO.output(in_2,GPIO.LOW)
    print("right turn")
    #for motor B 
    GPIO.output(en_b,GPIO.HIGH)
    GPIO.output(in_3,GPIO.LOW)
    GPIO.output(in_4,GPIO.LOW)
    


    

#function for left turn
#en_a = 1, in_0 = 1, in_2 = 0 for motor A
#en_b = 1, in_3 = 1, in_4 = 0 for motor B
#left motor (A) will ramian stop and right motor (B) will move forword
def left_turn():

    setup()
    #for motor A 
    GPIO.output(en_a,GPIO.HIGH)
    GPIO.output(in_1,GPIO.LOW)
    GPIO.output(in_2,GPIO.LOW)
    
    #for motor B 
    GPIO.output(en_b,GPIO.HIGH)
    GPIO.output(in_3,GPIO.HIGH)
    GPIO.output(in_4,GPIO.LOW)
    

    
#this function will move the camera left side
def cam_move_left():
    #function logic
    print("camera moved left")

#this function will move the camera right side
def cam_move_right():
    #function logic
    print("camera moved right")

#this function will move the camera upword side
def cam_move_upword():
    #function logic
    print("camera moved upword")

#this function will move the camera downword side
def cam_move_downword():
    #function logic
    print("camera moved downword")


# 
# 
# 
# def key(event):
#     if(event.char == 'w' or event.char == 'W'):
#         forword(0.05)
#     elif(event.char == 's' or event.char == 'S'):
#         backword(0.05)
#     elif(event.char == 'a' or event.char == 'a'):
#         left_turn(0.05)
#     elif(event.char == 'd' or event.char == 'D'):
#         right_turn(0.05)
#     elif(event.char == 'i' or event.char == 'I'):
#         cam_move_upword()
#     elif(event.char == 'k' or event.char == 'K'):
#         cam_move_downword()
#     elif(event.char == 'j' or event.char == 'J'):
#         cam_move_left()
#     elif(event.char == 'l' or event.char == 'L'):
#         cam_move_right()
#     else:
#         print("You pressed", event.char ,"please see the instractions ")
#


#this fuction will call when the pressed key will release
def on_key_release(event):
    global has_prev_key_release
    has_prev_key_release = None
    #print ("on_key_release", repr(event.char))
    #print("car forword stop")
    GPIO.cleanup()


#this fuction will call when any key will pressed
def on_key_press(event):
    #print ("on_key_press", repr(event.char))
    if event.char == "w" or event.char == "W":
        forword()
    elif event.char == "s" or event.char == "S":
        backword()
    elif event.char == "a" or event.char == "A":
        left_turn()
    elif event.char == "d" or event.char == "D":
        right_turn()
    
    elif event.char == "i" or event.char == "I":
        cam_move_upword()
    elif event.char == "k" or event.char == "K":
        cam_move_downword()
    elif event.char == "j" or event.char == "J":
        cam_move_left()
    elif event.char == "l" or event.char == "L":
        cam_move_right()
    else :
        print("please give correct input")






#this both function will manage above 2 function 
def on_key_release_repeat(event):
    global has_prev_key_release
    has_prev_key_release = root.after_idle(on_key_release, event)
    #print ("on_key_release_repeat", repr(event.char))


#this both function will manage above 2 function 
def on_key_press_repeat(event):
    global has_prev_key_release
    if has_prev_key_release:
        root.after_cancel(has_prev_key_release)
        has_prev_key_release = None
        #print ("on_key_press_repeat", repr(event.char))
    else:
        on_key_press(event)

def callback(event):
   frame.focus_set()
    #print ("clicked at", event.x, event.y)
    
frame = Frame(root, width=400, height=200)
frame.bind("<KeyRelease>", on_key_release_repeat)
frame.bind("<KeyPress>", on_key_press_repeat)
frame.bind("<KeyRelease>", on_key_release_repeat)
frame.bind("<KeyPress>", on_key_press_repeat)
#frame.pack()
frame.focus_set()
text= "Welcome to my project \n \n How to perate my car?? \n \n press 'w' for forward, 'a' for right turn, 'd' for left ture, 's' for backword \n\n 1 for increase the speed and 0 for decrease the speed "
Label(root, justify=LEFT, padx = 1, pady = 10, text=text).pack(side="top")
frame.pack()
root.mainloop()
    

    

# forword(1)
# backword(1)
# right_turn(0.5)
# left_turn(0.5)


