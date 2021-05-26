from flask import Flask, render_template, flash, redirect

app = Flask(__name__)
app.secret_key = "phieD2ooweejee6beerohpooTei1uiK"

@app.route("/")
def base():
	return  render_template("base.html")

@app.route("/messagepage")
def message():
	flash("This is a secret message")
	return redirect("/")

@app.route("/othermsg")
def beepboop():
	flash("Flash kikkailua")
	return redirect("/")

app.run()
