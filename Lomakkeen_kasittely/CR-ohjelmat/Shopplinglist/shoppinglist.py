from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key ="Eigae6thiemae4ShuneeWue0OhfaiTe"

class Shoppinglist(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	product = db.Column(db.String, nullable=False)
	amount = db.Column(db.Integer, nullable=False)

ShoppinglistForm = model_form(Shoppinglist, base_class = FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()
	shoppinglist = Shoppinglist(product = "Kaljaa", amount=12)
	db.session.add(shoppinglist)
	shoppinglist = Shoppinglist(product = "Porkkanoita", amount=5)
	db.session.add(shoppinglist)

	db.session.commit()

@app.route("/add", methods= ["GET", "POST"])
def addProduct():
	form = ShoppinglistForm()
	
	if form.validate_on_submit():
		shoppinglist = Shoppinglist()
		form.populate_obj(shoppinglist)
		
		db.session.add(shoppinglist)
		db.session.commit()

	return render_template("add.html", form=form)

@app.route("/")
def index():
	shoppinglists = Shoppinglist.query.all()
	return render_template("index.html", shoppinglists = shoppinglists)

app.run()
