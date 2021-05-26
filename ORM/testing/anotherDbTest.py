from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	director = db.Column(db.String, nullable=False)
	rating = db.Column(db.String, nullable=False)

@app.before_first_request
def initMe():
	db.create_all()
	movie = Movie(name = "Hard ticket to Hawaii", director="Andy Sidaris", rating="4.3")
	db.session.add(movie)

	db.session.commit()

@app.route("/")
def index():
	movies = Movie.query.all()
	return render_template("index.html", movies=movies)

if __name__ == "__main__":
	app.run()
