from flask import Flask, render_template
from flask import request

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/multiplicar")
def multiplicar():
    
    return render_template("multiplicar.html")

@app.route("/resultado", methods = ["POST"])
def resultado():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    res = int(n1 * n2)
    return render_template("resultado.html", n1 = n1, n2 = n2, res = res)

if __name__ == "__main__":
    app.run(debug = True)