from flask import Flask, render_template, request

import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 40

ledst = 0


GPIO.setup(led, GPIO.OUT)   

GPIO.output(led, GPIO.LOW)

@app.route("/")
def home():
    
    ledst = GPIO.input(led)
    templateData = {
              
              'ledSta'  : ledst,
        }
    
    return render_template("index2.html" ,**templateData)

@app.route("/<call>")
def action(call):
    if call == "on":
        GPIO.output(led, GPIO.HIGH)
    if call == "off":
        GPIO.output(led, GPIO.LOW)
        
        
    ledst = GPIO.input(led)
    
   
    templateData = {
              'ledSta'  : ledst,
              
    }
    
    return render_template('index2.html', **templateData)

        

if __name__ == "__main__":
   app.run(debug=True)