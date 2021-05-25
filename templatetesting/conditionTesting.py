from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
	return render_template("base.html")

@app.route("/ifpage")
def ifpage():
	things = ["car", "cat","banana"]
	return render_template("ifpage.html", things=things)

app.run()
