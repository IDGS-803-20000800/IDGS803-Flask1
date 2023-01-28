from flask import Flask, render_template

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/")
def index():
    nombre = "Filemona"
    lista1 = ["Español", "Inglés", "Química"]
    return render_template("index.html" str nombre, Lista[str] item)

@app.route("/usuarios")
def usuarios():
    return render_template("archivo2.html")

if __name__ == "__main__":
    app.run(debug = True)