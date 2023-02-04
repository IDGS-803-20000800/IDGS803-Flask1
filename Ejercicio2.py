#Realizar las operaciones básicas con lo visto en los temas 1 a 4
from flask import Flask
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/cinepolis", methods = ["GET", "POST"])
def cinepolis ():
    return render_template("")