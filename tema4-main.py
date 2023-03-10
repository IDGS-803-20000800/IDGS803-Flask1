from flask import Flask
from flask import request

app = Flask(__name__)

#Se pone la ruta en la que se ejecuta la aplicación
@app.route("/operasBas", methods = ["GET", "POST"])
def operasBas():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")   
        return "La suma es: {}".format(str(int(num1) + int(num2)))
    
    else:
        return '''
            <form action = "/operasBas" method = "POST"> 
            <label>N1: </label>
            <input type = "text" name = "num1"/><br></br>
            <label>N2: </label>
            <input type = "text" name = "num2"/><br></br>
            <button name = "button1" onClick = operasBas()/>
            </form>
    '''

if __name__ == "__main__":
    app.run(debug = True)