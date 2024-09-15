from flask import Flask, render_template



app = Flask(__name__)
@app.route("/")
def first_flask():
    return "This is my first Flask Program"

@app.route("/", methods = ["GET", "POST"])
def login():
    #Check if user id and password exist in database and match

@app.route("/flask_two")
def flask_two():
    return "Python is fun"

@app.route("/index")
def index():
    return render_template("index.html", name = "Aaron")

app.run(debug = True)