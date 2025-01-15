from ADQUISICION_DATOS.obtencion_inicial import obtener_datos_normalizados
from CONTROLADORES_GLOBALES.configuracion import cargar_configuracion
from NUCLEO_SINAPTICO.entrenamiento import entrenar_modelo
from NUCLEO_SINAPTICO.inferencia import predecir
import os

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
    datos_normalizados = obtener_datos_normalizados(ruta_datos)

    # Entrenar modelo
    modelo = entrenar_modelo(datos_normalizados, configuracion)

    # Guardar el modelo
    ruta_modelo = configuracion['ruta_modelo']
    modelo.save(os.path.join(ruta_modelo, 'modelo.h5'))

    # Realizar predicciones
    ventana = 100  # Tamaño de la ventana de datos históricos
    predicciones = predecir(modelo, datos_normalizados, ventana)
    print(predicciones)
    
    # Guardar predicciones
    ruta_predicciones = configuracion['ruta_predicciones']
    guardar_predicciones(predicciones, ruta_predicciones)

if __name__ == '__main__':
    main()
