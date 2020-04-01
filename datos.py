import pandas as pd
import pymongo
from pymongo import MongoClient

def capturaDatos():

    #Leemos los datos, desde los ficheros csv, tanto de temperatura, como de humedad.
    temperatura = pd.read_csv("./data/temperature.csv")
    humedad = pd.read_csv("./data/humidity.csv")

    #Indicamos, que queremos San Francisco para hacer la preedición
    temperatura= temperatura[['datetime','San Francisco']]
    humedad= humedad[['datetime','San Francisco']]

    # Debido a que en el fichero de tº y de humedad, la variable SanFrancisco se llama igual, le cambiamos el nombre.
    temperatura= temperatura.rename(columns={'San Francisco': 'temp'})
    humedad= humedad.rename(columns={'San Francisco': 'hum'})

    # Unimos los dos la temperatura, y la humedad, por la fecha.
    SF= pd.merge(temperatura,humedad, on= 'datetime')
    SF= SF.dropna() # Eliminamos los posibles NA que haya.
    SF= SF.tail(500) #Se pone por que tarda mucho y hay que coger un volumen mas pequeño de datos

    # Hacemos la conexión con mongoDB, a la base de datos, y a la coleccion
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["SanFrancisco"]
    col= db["Forecast"]

    #?
    SF.reset_index(inplace=True)
    data_dict=SF.to_dict("records")
    col.insert_many(data_dict)

if __name__ == '__main__':
    capturaDatos()
    print("Done :)")