"""
when you run the program and type localhost:5000 in browser the led will on and /about led off



"""
from flask import Flask, render_template, Response, request, redirect,url_for
import RPi.GPIO as GPIO
import time

led_1 = 40

ledst = 0

GPIO.setwarnings(False) #to desable the warning
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led_1, GPIO.OUT)

GPIO.output(led_1, GPIO.LOW)


app = Flask(__name__)

    

@app.route("/")
def homepage():
    
    ledst = GPIO.input(led_1)
    templateData = {
              
              'ledstatues'  : ledst,
              
        }
    
    return render_template("page.html", **templateData)


#     
# @app.route("/off")
# def off():
#     
#     GPIO.output(led_1,GPIO.LOW)
#     return render_template("home.html")
#     
# 
# @app.route("/on")
# def on():
#     GPIO.output(led_1,GPIO.HIGH)
#     return render_template("about.html")
# 

if __name__ == '__main__':
    app.run(debug=True)
    