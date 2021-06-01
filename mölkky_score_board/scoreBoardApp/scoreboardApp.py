from flask import Flask, render_template, flash, redirect, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key ="me9Ueg5ajie7Eogohqu9ma8seethoh"

class Game(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	participant = db.Column(db.Text, nullable=False)
	score = db.Column(db.Integer, nullable=False)
	rounds = db.Column(db.Integer, nullable=False)
	app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///ottokorhonen"

GameForm = model_form(Game, base_class=FlaskForm, db_session=db.session)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False, unique=True)
	passwordHash = db.Column(db.String, nullable=False)

	def setPassword(self, password):
		self.passwordHash = generate_password_hash(password)

	def checkPassword(self, password):
		return check_password_hash(self.passwordHash, password)

class UserForm(FlaskForm):
	email = StringField("email", validators=[validators.Email()])
	password = PasswordField("password", validators=[validators.InputRequired()])

def currentUser():
	try:
		uid = int(session["uid"])
	except:
		return None
	return User.query.get(uid)

app.jinja_env.globals["currentUser"] = currentUser

@app.before_first_request
def initDb():
	db.create_all()

	game = Game(name="Ensimmäinen peli", participant="Batman, Robin, Joker, Mr. Freeze", score=50, rounds=5)
	db.session.add(game)

	game = Game(name="Batmanin revanssipeli", participant="Batman, Mr.Freeze", score=50, rounds=10)
	db.session.add(game)

	db.session.commit()

@app.errorhandler(404)
def custom404(e):
	return render_template("404.html")

def loginRequired():
	if not currentUser():
		abort(403)

@app.route("/game/<int:id>/edit", methods=["GET", "POST"])
@app.route("/add", methods=["GET", "POST"])
def addView(id=None):
	loginRequired()
	game = Game()

	if id:
		game = Game.query.get_or_404(id)

	fields = GameForm(obj=game)

	if fields.validate_on_submit():
		fields.populate_obj(game)
		db.session.add(game)
		db.session.commit()

		flash("New game added!")
		return redirect("/")

	return render_template("add.html", fields=fields)

@app.route("/game/<int:id>/delete")
def deleteView(id):
	game = Game.query.get_or_404(id)
	db.session.delete(game)
	db.session.commit()

	flash("Game deleted!")
	return redirect("/")

@app.route("/")
def indexView():
	games = Game.query.all()
	return render_template("index.html", games=games)

@app.route("/user/login", methods=["GET", "POST"])
def loginView():
	form = UserForm()

	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		user = User.query.filter_by(email=email).first()
		if not user:
			flash("Login failed. No such user!")
			return redirect("/user/login")
		if not user.checkPassword(password):
			flash("Failed to login. Password not correct")
			return redirect("/user/login")

		session["uid"] = user.id
		flash("Logged in!")
		return redirect("/")

	return render_template("login.html", form=form)

@app.route("/user/register", methods=["GET", "POST"])
def registerView():
	form = UserForm()

	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		if User.query.filter_by(email=email).first():
			flash("User already exists. Please login!")
			return redirect("user/login")

		user = User(email=email)
		user.setPassword(password)

		db.session.add(user)
		db.session.commit()

		flash("Registration successful!")
		return redirect("/user/login")

	return render_template("register.html", form=form)

@app.route("/user/logout")
def logoutView():
	session["uid"] = None
	flash("Logged out!")
	return redirect("/")

@app.route("/instructions")
def instructionsView():
	return render_template("instructions.html")

app.run()
