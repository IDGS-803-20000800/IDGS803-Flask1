#Realizar las operaciones básicas con lo visto en los temas 1 a 4
from flask import Flask
from flask import request

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/operasBas", methods = ["GET", "POST"])
def operasBas():
    if request.method == "POST":
        opcion = request.form.get("rBOperacion")
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        match opcion :
            case "suma":
                return "La suma es: {}".format(str(int(num1) + int(num2)))
            case "resta":
                return "La resta es: {}".format(str(int(num1) - int(num2)))
            case "multiplicacion":
                return "La multiplicación es: {}".format(str(int(num1) * int(num2)))
            case "division":
                return "La división es: {}".format(str(int(num1) / int(num2)))
    
    else:
        return '''
            <form action = "/operasBas" method = "POST"> 
            <label>N1: </label>
            <input type = "text" name = "num1"/><br></br>
            <label>N2: </label>
            <input type = "text" name = "num2"/><br></br>
            <input type = "radio" value = suma name = "rBOperacion"/>Suma<br></br> 
            <input type = "radio" value = resta name = "rBOperacion"/>Resta<br></br>
            <input type = "radio" value = multiplicacion name = "rBOperacion"/>Multiplicación<br></br>
            <input type = "radio" value = division name = "rBOperacion"/>División<br></br>
            <input type = "submit" name = "button1" onClick = operasBas()/>Calcular operación
            </form>
    '''

if __name__ == "__main__":
    app.run(debug = True)