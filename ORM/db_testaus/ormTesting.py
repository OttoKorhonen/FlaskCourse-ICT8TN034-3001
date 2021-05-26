from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)

@app.before_first_request
def initMe():
	db.create_all()
	comment = Comment(text="Heipparallaa", name="Otto")
	db.session.add(comment)

	db.session.commit()

@app.route("/")
def index():
	comments = Comment.query.all()
	return render_template("index.html", comments=comments)

if __name__ =="__main__":
	app.run()
