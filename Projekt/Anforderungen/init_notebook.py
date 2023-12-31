import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def get_file_path():
    file_path = str(os.getcwd()).split("\Projekt")
    return file_path[0] + '\\Projekt\\Daten'



def get_initial_dataset():
    file_path = get_file_path()
    if os.path.exists(file_path + '\\smoking_driking_dataset_Ver01.csv'):
        dataset = pd.read_csv(file_path + '\\smoking_driking_dataset_Ver01.csv')
        return dataset
    else:
        print('Die Datei "smoking_driking_dataset_Ver01.csv" existiert nicht im Ordnerpfad ./Projekt/Daten' )
    


def get_final_dataset():
    file_path = get_file_path()
    if os.path.exists(file_path + '\\smoking_driking_dataset_Ver02.csv'):
        dataset = pd.read_csv(file_path + '\\smoking_driking_dataset_Ver02.csv')
        dataset = dataset.drop(columns=['Unnamed: 0'])
        return dataset
    else:
        print('Die Datei "smoking_driking_dataset_Ver02.csv" existiert nicht im Ordnerpfad ./Projekt/Daten' )



def minmax_scale_columns(df):
    # Kopie des ursprünglichen DataFrame erstellen, um das Original nicht zu ändern
    df_scaled = df.copy()
    
    # MinMaxScaler erstellen
    scaler = MinMaxScaler(feature_range=(0, 10))
    
    # Jede Spalte skalieren
    for column in df.columns:
        # Überprüfen, ob es sich um numerische Daten handelt (zum Beispiel nicht um Objekte wie Strings)
        if pd.api.types.is_numeric_dtype(df[column]):
            # Spalte skalieren
            df_scaled[column] = scaler.fit_transform(df[[column]])
    
    return df_scaled, scaler