"""
this is my first program
simple webpage using flask python

"""

from flask import Flask #import module 
app = Flask(__name__) #create object of flask 


@app.route("/")
#@app.route("/home")   #name of the page see in url

def home():
    return "<h1>Home Page hello fucking world</h1>"

@app.route("/about") # if you are defineing function like bellow the @app.route() is mendedary
def about():
    return "<h1>About Page</h1>"



if __name__ == '__main__':
    app.run(debug=True)  
