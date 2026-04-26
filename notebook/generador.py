import pandas as pd
import os

def crear_JSON(dataframe, nombre_archivo):
    # Esto asegura que se guarde en la carpeta 'data' del proyecto
    ruta = os.path.join("data", nombre_archivo)
    dataframe.to_json(ruta, orient="records", indent=4)
    print(f"Datos guardados en {ruta}")

def crear_csv(dataframe, nombre_archivo):
    # Guarda un DataFrame como archivo CSV en la carpeta 'data'.
    ruta = os.path.join("data", nombre_archivo)
    dataframe.to_csv(ruta, index=False)
    print(f"Datos guardados en {ruta}")
    