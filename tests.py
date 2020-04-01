import unittest
from predecir import predecirModelo 
from modelo import crearModelo
from datos import capturaDatos
import app as app
from sklearn.externals import joblib

class tests(unittest.TestCase):

    #Generamos tests para la captura de los datos.
    def test_datos(self):
        try:
            capturaDatos()
        except ExceptionType:
            self.fail("No se han capturado los datos de forma correcta: ERROR")

    #Generamos tests para el calculo del modelo
    def test_modelo(self):
        try:
            crearModelo()
        except ExceptionType:
            self.fail("No se ha creado el modelo de forma correcta: ERROR")
    
    #Generamos tests para la predicción dde la temperatura y la humedad
    def test_predecir(self):
        try:
            predecirModelo(24)
        except ExceptionType:
            self.fail("No se ha predicho el tiempo de forma correcta: ERROR")

    #Esta test esta centrado en la APIREST.

    #Test para el indice, comprobamos que no hay error.
    def test_index(self):
        response,ok=app.indice()
        self.assertEqual(ok, 200)
    
    #Test para la prediccion de 24 horas
    def test_24horas(self):
        response,ok=app.predecir24()
        self.assertEqual(ok, 200)
    
    #Test para la prediccion de 48 horas
    def test_48horas(self):
        response,ok=app.predecir48()
        self.assertEqual(ok,200)

    #Test para la prediccion de 72 horas
    def test_72horas(self):
        response,ok=app.predecir72()
        self.assertEqual(ok, 200)
    

if __name__ == '__main__':
    unittest.main()