import numpy as np
import pandas as pd
import datetime
from pymongo import MongoClient

def get_data_glucose(date1, date2):
    
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

def get_data_hemoglobine(date1, date2):
    
    #creamos los datos de glucosa para un dia y los hacemos dataframe
    data = []
    for _ in range(1,367):
        s = pd.DataFrame(np.random.poisson(3, 24))
        data.append(s)
    hb = pd.concat(data).reset_index()
    hb.drop(["index"], inplace = True, axis = 1)
        
    # creamos las fechas y las horas (frecuencia de una hora) y convertimos a dataframe
    mydates = pd.date_range(date1, date2,  freq='H').tolist()
    df2 = pd.DataFrame(mydates)
    # concatenamos los dataframes
    final = pd.concat([hb, df2], axis = 1)
    
    # limpieza
    final.columns = ["Hb", "Date"]
    
    final = final.dropna()
    final.set_index("Date")
    return final

def clean_date(df, col):
    df['Dates'] = pd.to_datetime(df[col]).dt.date
    df['Time'] = pd.to_datetime(df[col]).dt.time

    df['year']= df['Date'].dt.year
    df['month']= df['Date'].dt.month
    df['day']= df['Date'].dt.day
    df['hour']= df['Date'].dt.hour

    df.drop(["Dates", "Date", "Time"], axis = 1, inplace = True )
    return df


def hb (col):
    if col in range(0,71):
        return 4
    elif col in range(71,101):
        return 5
    elif col in range(101,127):
        return 6
    elif col in range(127,153):
        return 7
    elif col in range(153,184):
        return 8
    elif col in range(184,213):
        return 9
    elif col in range(213,241):
        return 10
    elif col in range(241,270):
        return 11
    else:
        return 12
    
def insert_data (df, nombre):
      
    client = MongoClient()
    db = client.Diabetes
    collection = db.create_collection(name = f"{nombre}")
    collection = db[f"{nombre}"]

    data = df.to_dict(orient='records')
    #print(data)
    collection.insert_many(data)
    
    return "Done"