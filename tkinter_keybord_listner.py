from tkinter import *
#from Tkinter import *
#import tkinter as tk 
#from colorama import Fore,Back

root = Tk()

def forword():
    print("forword")

def left_turn():
    print("left")

def right_turn():
    print("right")
     
def backword():
    print("backword")
     
def cam_move_right():
    print("camera move right")

def cam_move_left():
    print("camera move left")
    

def cam_move_up():
    print("camera move up")

def cam_move_down():
    print("camera move down")

def key(event):
    #print ("pressed", repr(event.char))
    if(event.char == 'w'):
        
        forword()
    
    elif(event.char == 'a'):
        left_turn()
        
    elif(event.char == 'd'):
        right_turn()
        
    elif(event.char == 's'):
        backword()
        
    elif(event.char == '4'):
        cam_move_left()
    elif(event.char == '6'):
        cam_move_right()
        
    elif(event.char == '8'):
        cam_move_up()
        
    elif(event.char == '2'):
        cam_move_down()
        
    elif(event.char == ' '):
        print("car stoped")
        
    else:
        print("You pressed", event.char ,"please see the instractions ")
    
        


        
def callback(event):
    frame.focus_set()
    #print ("clicked at", event.x, event.y)

frame = Frame(root, width=400, height=200)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)

text= "Welcome to my project \n \n How to perate my car?? \n \n press 'w' for forward, 'a' for right turn, 'd' for left ture, 's' for backword, 'space bar' for stop the car "

Label(root, justify=LEFT, padx = 1, pady = 10, text=text).pack(side="top")

frame.pack()

root.mainloop()


 
