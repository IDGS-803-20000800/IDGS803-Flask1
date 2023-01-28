from flask import Flask

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/")
def index():
    return "!!!!Hola Mundo¡¡¡¡ Otra cosa"

if __name__ == "__main__":
    app.run(debug = True)