'''
    Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define actuators GPIOs
ledRed = 13

#initialize GPIO status variables
ledRedSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   

# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)

    
@app.route("/")
def index():
    # Read Sensors Status
    ledRedSts = GPIO.input(ledRed)
 
    templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
              
        }
    return render_template('index.html', **templateData)
    
@app.route("/<action>")
def action( action):
  
   
   
    if action == "on":
        GPIO.output(ledRed, GPIO.HIGH)
    if action == "off":
        GPIO.output(ledRed, GPIO.LOW)
             
    ledRedSts = GPIO.input(ledRed)

   
    templateData = {
              'ledRed'  : ledRedSts,
             
    }
    return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(debug=True)