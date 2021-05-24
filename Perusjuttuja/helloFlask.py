from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world!"


@app.route("/hei")
def hei():
	return "Heippa"

if __name__  == "__main__":
	app.run()
