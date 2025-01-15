from ADQUISICION_DATOS.obtencion_inicial import obtener_datos_normalizados
from CONTROLADORES_GLOBALES.configuracion import cargar_configuracion
from NUCLEO_SINAPTICO.entrenamiento import entrenar_modelo
from NUCLEO_SINAPTICO.inferencia import predecir
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def normalizar_datos(datos):
    scaler = MinMaxScaler()
    datos_normalizados = scaler.fit_transform(datos)
    return datos_normalizados, scaler

def generar_ventanas(datos, ventana):
    X, y = [], []
    for i in range(len(datos) - ventana):
        X.append(datos[i:i + ventana])
        y.append(datos[i + ventana])
    return np.array(X), np.array(y)

def guardar_predicciones(predicciones, ruta):
    with open(ruta, 'w') as file:
        for prediccion in predicciones:
            file.write(f"{prediccion}\n")

def main():
    # Cargar configuración
    configuracion = cargar_configuracion('configuracion.json')

    # Crear directorios para el modelo y checkpoints si no existen
    os.makedirs(configuracion['ruta_modelo'], exist_ok=True)
    os.makedirs(configuracion['ruta_checkpoints'], exist_ok=True)

    # Obtener datos normalizados
    ruta_datos = configuracion['ruta_datos']
    datos = obtener_datos_normalizados(ruta_datos)
    datos_normalizados, scaler = normalizar_datos(datos)

    # Generar ventanas de datos
    ventana = configuracion['ventana']
    X, y = generar_ventanas(datos_normalizados, ventana)

    # Entrenar modelo
    modelo = entrenar_modelo(X, y, configuracion)

    # Guardar el modelo
    ruta_modelo = configuracion['ruta_modelo']
    modelo.save(os.path.join(ruta_modelo, 'modelo.h5'))

    # Realizar predicciones
    predicciones = predecir(modelo, X)
    predicciones_desnormalizadas = scaler.inverse_transform(predicciones)
    print(predicciones_desnormalizadas)
    
    # Guardar predicciones
    ruta_predicciones = configuracion['ruta_predicciones']
    guardar_predicciones(predicciones_desnormalizadas, ruta_predicciones)

if __name__ == '__main__':
    main()
