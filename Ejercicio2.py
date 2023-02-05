#Realizar las operaciones básicas con lo visto en los temas 1 a 4
from flask import Flask
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/")
def cinepolis ():
    return render_template("cinepolis.html")
    

@app.route("/procesar", methods = ["GET", "POST"])
def calcularCosto():
    cantidadCompradores = request.form.get("numCompradores")
    tarjetaCineco = request.form.get("tarjetaCineco")
    cantidadBoletos = request.form.get("numBoletos")
    descuento = 0
    descuentoCineco = 0
    costoTotal = ""
    if float(cantidadBoletos) > float(cantidadCompradores) * 7:
        costoTotal = "La cantidad de boletos a comprar es mayor a la aceptada"
        return render_template("costo.html", costoTotal = costoTotal)
    if tarjetaCineco == '1':
        descuentoCineco = descuentoCineco + .10
    if float(cantidadBoletos) >= 3 and float(cantidadBoletos) <= 5:
        descuento = descuento +.10
    elif float(cantidadBoletos) > 5:
        descuento = descuento +.15
    else: descuento = 0
    costoTotal = "El costo total es: {}".format(((float(cantidadBoletos)*12)*(1-descuento))*(1-descuentoCineco))
    return render_template("costo.html", costoTotal = costoTotal)

if __name__ == "__main__":
    app.run(debug = True)