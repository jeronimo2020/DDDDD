import json
import os

def cargar_configuracion(ruta_config):
    """
    Carga la configuración desde un archivo JSON.

    Args:
        ruta_config (str): Ruta del archivo de configuración.

    Returns:
        dict: Configuración cargada.
    """
    try:
        # Leemos el archivo JSON
        with open(ruta_config, 'r') as file:
            configuracion = json.load(file)
        return configuracion
    except Exception as e:
        print(f"Error al cargar la configuración: {e}")
        return None

def cache(config):
    print("Almacenando configuración en cache...")
    cache_storage = config  # En un escenario real, se podría usar algo como Redis o un archivo temporal
    print("Configuración almacenada en cache")
    return cache_storage

def gestor_parametros(config, key, default=None):
    print(f"Obteniendo parámetro '{key}'...")
    return config.get(key, default)

def parser(config_path):
    print(f"Parseando configuración desde {config_path}...")
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
        print("Configuración parseada")
        return config
    except Exception as e:
        print(f"Error al parsear configuración: {e}")
        return {}

def serializador(config, config_path):
    print(f"Serializando configuración en {config_path}...")
    try:
        with open(config_path, 'w') as file:
            json.dump(config, file)
        print("Configuración serializada")
        return config_path
    except Exception as e:
        print(f"Error al serializar configuración: {e}")
        return None

def validador_config(config):
    print("Validando configuración...")
    required_keys = ["ruta_datos", "ruta_modelo", "ruta_checkpoints", "ruta_predicciones", "ventana", "parametros_entrenamiento"]
    for key in required_keys:
        if key not in config:
            print(f"Falta la clave requerida: {key}")
            return False
    print("Configuración validada")
    return True
