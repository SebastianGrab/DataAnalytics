import pandas as pd
import os
import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns


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
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Jede Spalte skalieren
    for column in df.columns:
        # Überprüfen, ob es sich um numerische Daten handelt (zum Beispiel nicht um Objekte wie Strings)
        if pd.api.types.is_numeric_dtype(df[column]):
            # Spalte skalieren
            df_scaled[column] = scaler.fit_transform(df[[column]])
    
    return df_scaled, scaler



# Funktion zur Ausgabe der Modellmetriken:

def evaluate_clustering_metrics(dataset, kmeans_model):

    # Clustering-Evaluierungsmetriken berechnen
    hom = metrics.homogeneity_score(dataset['Cluster'], kmeans_model.labels_)
    com = metrics.completeness_score(dataset['Cluster'], kmeans_model.labels_)
    vmeasure = metrics.v_measure_score(dataset['Cluster'], kmeans_model.labels_)

    # Ausgabe der Metriken
    print(f"Homogeneity Score: {hom}")
    print(f"Completeness Score: {com}")
    print(f"V-Measure Score: {vmeasure}")



# Funktion zum Trainieren eines KMeans Modell mit Ausgabe von Metriken:

def cluster_n_print(dataset, c, r, i):
    kmeans = KMeans(n_clusters=c, random_state=r, n_init=i)
    dataset['Cluster'] = kmeans.fit_predict(dataset)
    print("-" * 40)  # waagerechter Strich oben
    print(f"Inertia: {kmeans.inertia_}\n"
          f"n_clusters= {kmeans.n_clusters}\n"
          f"random_state= {kmeans.random_state}\n"
          f"n_init= {kmeans.n_init}")
    print("-" * 40)  # waagerechter Strich unten



# Funktion zum Trainieren eines KMeans Modell mit Ausgabe von Metriken, Modell & Datensatz:

def cluster_n_print_ver2(dataset, c, r, i):
    kmeans = KMeans(n_clusters=c, random_state=r, n_init=i)
    dataset['Cluster'] = kmeans.fit_predict(dataset)
    print("-" * 40)  # waagerechter Strich oben
    print("\n")
    print(f"Inertia: {kmeans.inertia_}\n"
          f"n_clusters= {kmeans.n_clusters}\n"
          f"random_state= {kmeans.random_state}\n"
          f"n_init= {kmeans.n_init}\n")
    print("Clustergrößen: ")
    for j in range(0,c):
      print("Name:", j, "Größe: ", list(kmeans.labels_).count(j))
    print("\n")
    print("-" * 40)  # waagerechter Strich unten
    return dataset, kmeans



# Funktion zum Trainieren eines KMeans Modell mit Ausgabe von Metriken, Modell & Datensatz:

def cluster_n_print_ver3(dataset, c, r, i):
    kmeans = KMeans(init="random", n_clusters=c, random_state=r, n_init=i)
    dataset['Cluster'] = kmeans.fit_predict(dataset)
    print("-" * 40)  # waagerechter Strich oben
    print("\n")
    print(f"Inertia: {kmeans.inertia_}\n"
          f"n_clusters= {kmeans.n_clusters}\n"
          f"random_state= {kmeans.random_state}\n"
          f"n_init= {kmeans.n_init}\n"
          f"init= {kmeans.init}\n")
    print("Clustergrößen: ")
    for j in range(0,c):
      print("Name:", j, "Größe: ", list(kmeans.labels_).count(j))
    print("-" * 40)  # waagerechter Strich unten
    return dataset, kmeans



# Funktionen zum Darstellen der Featureausprägungen je Cluster:

def cluster_analytics(df, clusterNo):

    columns =  df.columns.values.tolist()

    for column in columns:
        for i in range(0, clusterNo):
            dataset = df[df.Cluster == i]
            print(column + " max. - Cluster " + str(i) + ": " + str(dataset[column].max()))
            print(column + " min. - Cluster " + str(i) + ": " + str(dataset[column].min()))
            print(column + " med. - Cluster " + str(i) + ": " + str(dataset[column].median()))
            print(column + " mean - Cluster " + str(i) + ": " + str(dataset[column].mean()))
            print('')
        print('-'*35)
