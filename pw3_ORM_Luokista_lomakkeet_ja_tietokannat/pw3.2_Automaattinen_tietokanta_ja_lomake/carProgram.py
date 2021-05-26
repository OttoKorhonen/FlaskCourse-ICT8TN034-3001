from  flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key ="phieD2ooweejee6beerohpooTei1uiK"

class Car(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	brand = db.Column(db.String, nullable=False)
	model = db.Column(db.String, nullable=False)
	year = db.Column(db.Integer, nullable=False)
	fuel = db.Column(db.String, nullable=False)

CarForm = model_form(Car, base_class = FlaskForm, db_session = db.session)

@app.before_first_request
def initDb():
	db.create_all()
	car = Car(brand="Lada", model="Samara", year=1985, fuel="Gasoline")
	secondCar = Car(brand="Mercedes-Benz", model="C63 AMG", year=2021, fuel="Gasoline")
	db.session.add(car)
	db.session.add(secondCar)
	
	db.session.commit()

@app.route("/")
def base():
	cars = Car.query.all()
	flash("This is base page. Welcome!")
	return render_template("base.html", cars=cars) 

@app.route("/carform", methods=["GET", "POST"])
def carform():
	flash=("This is a form for adding a new car to the db")
	form = CarForm()
	return render_template("carform.html", form=form)

app.run()
