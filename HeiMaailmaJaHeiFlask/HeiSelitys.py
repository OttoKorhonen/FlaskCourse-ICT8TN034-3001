#tuodaan flask luokka käyttöön moduuleista
from flask import Flask

#luodaan app olio, joka on luotu Flask-luokasta.
#Flask-luokalle on annettu käyttöön __name__ parametri,
#ilmeisesti määrittelee, jos muuttujia on useampia mihin se viittaa
app = Flask(__name__)

#määritellään reitti, jota app-olio käyttää.
#Kun osoite on pelkkä / kutsutaan juttu-funktiota, joka palauttaa tekstin
@app.route("/")
def juttu():
    return "Heipähei käyttäjä"

#estää funktion kutsun vahingossa
if __name__ == "__main__":
    app.run()