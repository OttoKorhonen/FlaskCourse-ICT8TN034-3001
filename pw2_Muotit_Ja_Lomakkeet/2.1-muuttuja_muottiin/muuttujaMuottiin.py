from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
	thing = "I come from flask"
	return render_template("base.html", thing=thing)

app.run()
