# Composiciones

Este directorio contiene los diferentes procesos que se pueden ejecutar en el sistema. Cada proceso tiene su propio subdirectorio con un archivo `main.py`, un archivo de configuración `configuracion.json`, y dos subdirectorios (`modelos` y `checkpoints`) para guardar los modelos y checkpoints respectivamente.

## Crear un Nuevo Proceso

Para crear un nuevo proceso, sigue estos pasos:

1. **Crear un Subdirectorio**: Crea un nuevo subdirectorio dentro de `composiciones` con el nombre del proceso.
2. **Crear el Archivo `main.py`**: Crea un archivo `main.py` dentro del subdirectorio del proceso. Este archivo debe contener el flujo de trabajo del proceso.
3. **Crear el Archivo de Configuración**: Crea un archivo `configuracion.json` dentro del subdirectorio del proceso. Este archivo debe contener todas las configuraciones necesarias para los componentes que se van a utilizar.
4. **Crear Subdirectorios para Modelos y Checkpoints**: Crea dos subdirectorios dentro del subdirectorio del proceso: `modelos` y `checkpoints`. Estos subdirectorios se utilizarán para guardar los modelos y checkpoints respectivamente.
5. **Actualizar el Archivo de Configuración**: Asegúrate de que el archivo de configuración incluya las rutas a los subdirectorios `modelos` y `checkpoints`.

## Ejemplo de Proceso

```python
# main.py
from ADQUISICION_DATOS.obtencion_inicial import obtener_datos_normalizados
from CONTROLADORES_GLOBALES.configuracion import cargar_configuracion
from NUCLEO_SINAPTICO.entrenamiento import entrenar_modelo
from NUCLEO_SINAPTICO.inferencia import predecir
import os

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

if __name__ == '__main__':
    main()
```

## Agregar Nuevas Funciones o Componentes

Si el proceso requiere funciones o componentes en algunos de los módulos que no existen, sigue estos pasos:

1. **Identificar el Módulo**: Identifica el módulo al que pertenece la nueva función o componente.
2. **Agregar la Función o Componente**: Abre el archivo correspondiente al módulo y agrega la nueva función o componente.
3. **Actualizar el Archivo de Configuración**: Asegúrate de que el archivo de configuración incluya los parámetros necesarios para la nueva función o componente.

## Ejemplo de Agregar una Nueva Función

```python
# almacenamiento.py
def nueva_funcion(datos):
    # Implementación de la nueva función
    pass
```

```json
// configuracion.json
{
    "adquisicion_datos": {
        "almacenamiento": {
            "nueva_funcion": {
                "param1": "valor1",
                "param2": "valor2"
            }
        }
    }
}
```

## Actualizar un Proceso Existente

Para actualizar un proceso existente, sigue estos pasos:

1. **Modificar el Archivo `main.py`**: Realiza los cambios necesarios en el archivo `main.py` del proceso.
2. **Actualizar el Archivo de Configuración**: Si es necesario, actualiza el archivo `configuracion.json` con los nuevos parámetros o rutas.
3. **Verificar Subdirectorios**: Asegúrate de que los subdirectorios `modelos` y `checkpoints` estén actualizados y contengan los archivos necesarios.
4. **Probar el Proceso**: Ejecuta el proceso para verificar que los cambios funcionan correctamente.

Esta estructura y metodología te permitirá gestionar y ejecutar diferentes flujos de trabajo o procesos de manera organizada y eficiente, con la capacidad de agregar nuevas funciones o componentes según sea necesario.
