from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app=Flask(__name__)
db = SQLAlchemy(app)
app.secret_key="naiqu2ShaiS8beish0euna0lah7chu"

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	address = db.Column(db.String, nullable=False)
	phone = db.Column(db.String, nullable=False)
	favoriteSong = db.Column(db.String, nullable=False)
	favoriteShow = db.Column(db.String, nullable=False)

PersonForm = model_form(Person, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

	person = Person(name="Göran Petterson", email="g.petterson@gmail.com", address="Stockholmsgatan 4" , phone="+46 1233456", favoriteSong="Master of puppets", favoriteShow="Alla sjunger på Skansen")
	db.session.add(person)
	
	person = Person(name="Vladimir Putin", email="vladpu@kreml.ru", address="Moskovankatu1", phone="+7 987876423", favoriteSong="Venäjän federaation hymni", favoriteShow="Mythbusters")
	db.session.add(person)

	person = Person(name="Mikko Mallikas", email="mikko.mallikas@gmail.com", address="alfons åbergs gatan 3", phone="+46 78371323", favoriteSong="Sommar är kort", favoriteShow="Salatut elämät")
	db.session.add(person)

	db.session.commit()

@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/add", methods=["GET", "POST"])
def addPerson(id=None):
	person = Person()
	if id:
		person = Person.query.get_or_404(id)

	form = PersonForm(obj=person)

	if form.validate_on_submit():
		form.populate_obj(person)

		db.session.add(person)
		db.session.commit()

		flash("New person added to address book")
		return redirect("/")

	return render_template("add.html", form=form)


@app.route("/<int:id>/delete")
def delete(id):
	person = Person.query.get_or_404(id)
	db.session.delete(person)
	db.session.commit()

	flash("You have deleted a person from address book")
	return redirect("/")

@app.route("/")
def index():
	persons = Person.query.all()
	return render_template("index.html", persons=persons)

app.run()
