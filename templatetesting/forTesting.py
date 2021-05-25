from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	things =["cat", "car", "elephant"]
	return render_template("base.html", things=things)


app.run()
