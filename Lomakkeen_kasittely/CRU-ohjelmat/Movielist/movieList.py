from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = "neshah6pee8EeTief4ajough6fiezih"

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, primary_key=False)
	director = db.Column(db.String, nullable=False)
	rating = db.Column(db.Float, nullable=False)
	comment = db.Column(db.Text, nullable=True)

MovieForm = model_form(Movie, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

	movie = Movie(name="The Shawshank Redemption", director="Frank Darabont", rating=9.3, comment="Good movie. Beepboop.")
	db.session.add(movie)
	
	movie = Movie(name="The Godfather", director="Francis Ford Coppola", rating=9.2, comment="Other good movie.")
	db.session.add(movie)
	
	movie= Movie(name="The Godfather part II", director="Francis Ford Coppola", rating=9.0, comment="Beepboop")
	db.session.add(movie)

	db.session.commit()

@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/new", methods=["GET", "POST"])
def addMovie(id=None):
	movie = Movie()

	if id:
		movie = Movie.query.get_or_404(id)

	form = MovieForm(obj=movie)

	if form.validate_on_submit():
		form.populate_obj(movie)

		db.session.add(movie)
		db.session.commit()

		flash("New movie added")
		redirect("/")

	return render_template("new.html", form=form)

@app.route("/")
def index():
	movies = Movie.query.all()
	return render_template("index.html", movies=movies)

app.run()
