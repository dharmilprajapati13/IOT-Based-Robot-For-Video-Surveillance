"""
This is second program in which i have use templates directory to save html file 


"""

from flask import Flask,render_template #import module 
app = Flask(__name__) #create object of flask 


@app.route("/")
#@app.route("/home")   #name of the page see in url

def home():
    return render_template("home.html")

@app.route("/about") # if you are defineing function like bellow the @app.route() is mendedary
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)  
