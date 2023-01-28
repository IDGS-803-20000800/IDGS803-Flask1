from flask import Flask

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/user/<string: user>")
def index():
    return "!!!!Hola Mundo¡¡¡¡ "

@app.route("/numero/<int: n>")
def numero(n):
    return "Numero(xp) {}".format(n)

@app.route("/user/<int: id>/<string: name>")
def func(id, name):
    return "ID : {1} Nombre: {0}".format(id, name)

@app.route("/suma/<float: n1>/<float: n2")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

if __name__ == "__main__":
    app.run(debug = True)

if __name__ == "__main__":
    app.run(debug = True)