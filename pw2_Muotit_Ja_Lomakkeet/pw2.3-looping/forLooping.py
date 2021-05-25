from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
	header="This is base page"
	things = ["potato", "banana", "tomato", "carrot", "garlic"]
	return render_template("base.html", header=header, things=things)

@app.route("/index")
def index():
	header="This is index page and we are looping through things"
	things=["Lada Samara", "Door knob", "Keyboard", "Datsun 100 A", "The sun", "Leaf"]
	return render_template("index.html", header=header, things=things)

app.run()
