from flask import Flask

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/")
def index():
    return "!!!!Hola Mundo¡¡¡¡ Otra cosa"

@app.route("/hola")
def hola():
    return "<h1> saludo desde <h1>"

@app.route("/nueva")
def hola():
    return "<h1> saludo nueva <h1>"  

if __name__ == "__main__":
    app.run(debug = True)