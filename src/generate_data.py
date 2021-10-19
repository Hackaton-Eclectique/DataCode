import numpy as np
import pandas as pd
import datetime

def get_data(date1, date2):
    
    #creamos los datos de glucosa para un dia y los hacemos dataframe
    data = []
    for _ in range(1,367):
        s = pd.DataFrame(np.random.poisson(140, 24))
        data.append(s)
    glucose = pd.concat(data).reset_index()
    glucose.drop(["index"], inplace = True, axis = 1)
        
    # creamos las fechas y las horas (frecuencia de una hora) y convertimos a dataframe
    mydates = pd.date_range(date1, date2,  freq='H').tolist()
    df2 = pd.DataFrame(mydates)
    # concatenamos los dataframes
    final = pd.concat([glucose, df2], axis = 1)
    
    # limpieza
    final.columns = ["Glucose", "Date"]
    
    final = final.dropna()
    final.set_index("Date")
    return final