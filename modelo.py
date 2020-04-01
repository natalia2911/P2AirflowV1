import pandas as pd
import pymongo
from pymongo import MongoClient
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
from sklearn.externals import joblib

def crearModelo():

    # Hacemos la conexión con mongoDB, a la base de datos, y a la coleccion
    client = MongoClient("mongodb://0.0.0.0:27017")
    db = client["SanFrancisco"]
    col= db["Forecast"]
    
    # Elegimos los parametros del dataframe, de los cuales queremos predecir el modelo.
    dataframe = pd.DataFrame(list(col.find()))
    dataframe=dataframe[['datetime','temp','hum']]

    #Predecimos la temperatura con arima
    mTemperatura = pm.auto_arima(dataframe[['temp']], start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)

    print("Terminamos de generar el modelo de la Temperatura")
    #Lo almacenamos en un modelo
    joblib.dump(mTemperatura, './modelo/temperatura.pkl')

    #Predecimos la humedad, con arima
    mHumedad = pm.auto_arima(dataframe[['hum']], start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)

    print("Terminamos de generar el modelo de la Humedad")
    #Lo almacenamos en un modelo
    joblib.dump(mHumedad, './modelo/humedad.pkl')

if __name__ == '__main__':
    crearModelo()