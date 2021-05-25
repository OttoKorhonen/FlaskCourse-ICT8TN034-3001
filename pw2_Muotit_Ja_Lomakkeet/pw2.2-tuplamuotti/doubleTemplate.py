from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
	header = "This is base page"
	something = "Hello world!"
	return render_template("base.html", something = something, header=header)

@app.route("/index")
def index():
	header = "Hello Flask, this is index page"
	something="Flask is fun!"
	return render_template("index.html", something=something, header=header)

@app.route("/foobar")
def foobar():
	header = "Hello from foobar!"
	message = "This is message from Flask to the foobar page."
	return render_template("foobar.html", message = message, header=header)

app.run()
