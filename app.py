from whatsapp import getImage
from flask import Flask, request, url_for, render_template
app = Flask(__name__, template_folder='./front/')


@app.route('/')
def home():
    return render_template('main.html')


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/sub1.html")
def sub1():
    return render_template("sub1.html")


@app.route("/whatsapp")
def sub2():
    getImage()
    return "<h1>Please CLose the whatsapp tab and open the /collage link</h1>"


@app.route("/collage")
def sub3():
    return render_template("collage.html")
