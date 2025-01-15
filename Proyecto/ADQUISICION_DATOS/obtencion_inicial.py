import os
import pandas as pd
from glob import glob
import json
from sklearn.preprocessing import MinMaxScaler

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

def alinear_datos(datos):
    """
    Alinea los datos por marca de tiempo y elimina segmentos incompletos.
    
    Args:
        datos (dict): Diccionario con los datos organizados por pares de divisas.
    
    Returns:
        pd.DataFrame: DataFrame con los datos alineados y normalizados.
    """
    # Concatenar todos los DataFrames y alinear por marca de tiempo
    df_concatenado = pd.concat([df.set_index('timestamp') for dfs in datos.values() for df in dfs], axis=1)
    df_concatenado.dropna(axis=0, how='any', inplace=True)
    
    # Normalizar los datos
    df_normalizado = df_concatenado.apply(lambda x: (x - x.min()) / (x.max() - x.min()) * 100, axis=0)
    
    return df_normalizado

def obtener_datos_normalizados(ruta):
    """
    Obtiene y normaliza el conjunto de datos inicial.

    Args:
        ruta (str): Ruta del directorio principal.

    Returns:
        pd.DataFrame: El conjunto de datos normalizado.
    """
    try:
        # Cargar los datos desde un archivo CSV (puedes modificar el formato según tus necesidades)
        datos = pd.read_csv(ruta)

        # Suponiendo que los datos contienen valores numéricos que necesitamos normalizar
        scaler = MinMaxScaler()
        datos_normalizados = scaler.fit_transform(datos)
        
        # Convertimos el resultado a un DataFrame con los mismos nombres de columnas
        datos_normalizados_df = pd.DataFrame(datos_normalizados, columns=datos.columns)

        return datos_normalizados_df
    except Exception as e:
        print(f"Error al obtener los datos normalizados: {e}")
        return None

def conector(ruta_datos):
    print("Conectando a la fuente de datos...")
    if os.path.exists(ruta_datos):
        print(f"Conexión establecida a {ruta_datos}")
        return ruta_datos
    else:
        raise FileNotFoundError(f"La ruta {ruta_datos} no existe.")

def extractor(ruta_datos):
    print("Extrayendo datos...")
    archivos = [os.path.join(ruta_datos, archivo) for archivo in os.listdir(ruta_datos) if archivo.endswith('.json')]
    datos = []
    for archivo in archivos:
        try:
            with open(archivo, 'r') as file:
                datos.append(json.load(file))
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON en {archivo}: {e}")
        except Exception as e:
            print(f"Error al leer {archivo}: {e}")
    print("Datos extraídos")
    return datos

def gestor_errores(datos):
    print("Gestionando errores...")
    datos_limpios = [dato for dato in datos if 'error' not in dato]
    print(f"Errores gestionados: {len(datos) - len(datos_limpios)} errores encontrados y eliminados")
    return datos_limpios

def parser(datos):
    print("Parseando datos...")
    datos_parseados = []
    for dato in datos:
        try:
            datos_parseados.append({
                'fecha': dato['fecha'],
                'valor': float(dato['valor'])
            })
        except (KeyError, ValueError) as e:
            print(f"Error al parsear dato {dato}: {e}")
    print("Datos parseados")
    return datos_parseados

def validador(datos):
    print("Validando datos...")
    datos_validados = [dato for dato in datos if dato['valor'] >= 0]
    print(f"Datos validados: {len(datos_validados)} de {len(datos)} datos son válidos")
    return datos_validados
