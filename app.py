#!flask/bin/python
from flask import Flask
from predecir import predecirModelo 

app = Flask(__name__)

#Ruta indice "inicio"
@app.route('/')
def indice():
    salida = "<h1>Pronostico del tiempo: San Francisco</h1></br><a>Esta es la predicción del tiempo en San Francisco, esta predicción se ha realizado con Forecast</a></br></br><a href='http://127.0.0.1:5000/24horas'>Predicción día 1 (24 horas) </a></br><a href='http://127.0.0.1:5000/48horas'>Predicción día 2 (48 horas) </a></br><a href='http://127.0.0.1:5000/72horas'>Predicción día 3 (72 horas) </a>",200
    return salida

#Ruta para prediccion 24 horas
@app.route('/24horas')
def predecir24():
    salida = predecirModelo(24)
    return salida.to_html(),200

#Ruta prediccion de 48 horas
@app.route('/48horas')
def predecir48():
    salida = predecirModelo(48)
    return salida.to_html(),200

#Ruta prediccion 72 horas
@app.route('/72horas')
def predecir72():
    salida = predecirModelo(72)
    return salida.to_html(),200

if __name__ == '__main__':
    app.run(debug=True)