from sklearn.utils import resample
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Aquí puedes implementar funciones adicionales para la preparación final de los datos
# como balanceo, construcción de matrices, empaquetado, escalado y generación de ventanas.

def balanceador(datos):
    """
    Balancea los datos para asegurar una distribución uniforme.

    Args:
        datos (list): Lista de datos a balancear.

    Returns:
        list: Datos balanceados.
    """
    try:
        # Supongamos que tenemos clases desequilibradas, y balanceamos usando el muestreo de sobremuestreo
        datos_positivos = [d for d in datos if d['clase'] == 1]
        datos_negativos = [d for d in datos if d['clase'] == 0]

        # Realizamos sobremuestreo en los datos negativos para balancearlos con los positivos
        datos_negativos_balanceados = resample(datos_negativos, 
                                               replace=True,    
                                               n_samples=len(datos_positivos),    
                                               random_state=42)
        
        # Concatenamos los datos positivos con los negativos balanceados
        datos_balanceados = datos_positivos + datos_negativos_balanceados
        
        return datos_balanceados
    except Exception as e:
        print(f"Error al balancear los datos: {e}")
        return None

def constructor_matrices(datos):
    """
    Construye matrices a partir de los datos.

    Args:
        datos (list): Lista de datos.

    Returns:
        list: Matrices construidas.
    """
    try:
        # Suponemos que los datos son una lista de listas o un DataFrame que se debe convertir en matrices
        matrices = np.array(datos)  # Convierte la lista de datos en una matriz numpy
        return matrices
    except Exception as e:
        print(f"Error al construir las matrices: {e}")
        return None

def empaquetador(datos):
    """
    Empaqueta los datos para su almacenamiento o procesamiento.

    Args:
        datos (list): Lista de datos.

    Returns:
        dict: Datos empaquetados.
    """
    try:
        # Empaquetamos los datos en un diccionario
        datos_empaquetados = {
            "datos": datos,
            "timestamp": pd.to_datetime('now').strftime('%Y-%m-%d %H:%M:%S')
        }
        return datos_empaquetados
    except Exception as e:
        print(f"Error al empaquetar los datos: {e}")
        return None

def escalador(datos):
    """
    Escala los datos para normalizarlos.

    Args:
        datos (list): Lista de datos.

    Returns:
        list: Datos escalados.
    """
    try:
        # Usamos MinMaxScaler para escalar los datos
        scaler = MinMaxScaler()
        datos_escalados = scaler.fit_transform(datos)
        return datos_escalados
    except Exception as e:
        print(f"Error al escalar los datos: {e}")
        return None

def generador_ventanas(datos, ventana):
    """
    Genera ventanas de datos para el análisis temporal.

    Args:
        datos (list): Lista de datos.
        ventana (int): Tamaño de la ventana.

    Returns:
        list: Ventanas de datos.
    """
    try:
        ventanas = []
        for i in range(len(datos) - ventana + 1):
            ventana_datos = datos[i:i + ventana]
            ventanas.append(ventana_datos)
        return ventanas
    except Exception as e:
        print(f"Error al generar las ventanas de datos: {e}")
        return None
