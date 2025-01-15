import os
import pandas as pd
from glob import glob
import json

def leer_datos(ruta):
    """
    Lee todos los archivos XLSX en los subdirectorios de la ruta especificada.
    
    Args:
        ruta (str): Ruta del directorio principal.
    
    Returns:
        dict: Diccionario con los datos organizados por pares de divisas.
    """
    datos = {}
    for subdir, _, _ in os.walk(ruta):
        archivos = glob(os.path.join(subdir, '*.xlsx'))
        for archivo in archivos:
            par_divisa = os.path.basename(subdir)
            df = pd.read_excel(archivo)
            if par_divisa not in datos:
                datos[par_divisa] = []
            datos[par_divisa].append(df)
    return datos

def cache(datos):
    print("Almacenando en cache...")
    cache_storage = {}
    for i, dato in enumerate(datos):
        cache_storage[i] = dato
    print("Datos almacenados en cache")
    return cache_storage

def compressor(datos):
    print("Comprimiendo datos...")
    try:
        datos_comprimidos = [str(dato).encode('utf-8') for dato in datos]
        print("Datos comprimidos")
        return datos_comprimidos
    except Exception as e:
        print(f"Error al comprimir datos: {e}")
        return []

def gestor_archivos(datos, ruta_archivo):
    print("Gestionando archivos...")
    try:
        with open(ruta_archivo, 'w') as file:
            json.dump(datos, file)
        print(f"Datos guardados en {ruta_archivo}")
        return ruta_archivo
    except Exception as e:
        print(f"Error al guardar datos en {ruta_archivo}: {e}")
        return None

def indexador(datos):
    print("Indexando datos...")
    try:
        index = {i: dato for i, dato in enumerate(datos)}
        print("Datos indexados")
        return index
    except Exception as e:
        print(f"Error al indexar datos: {e}")
        return {}

def versionador(datos):
    print("Versionando datos...")
    try:
        version = 1
        versioned_data = {'version': version, 'datos': datos}
        print("Datos versionados")
        return versioned_data
    except Exception as e:
        print(f"Error al versionar datos: {e}")
        return {}
