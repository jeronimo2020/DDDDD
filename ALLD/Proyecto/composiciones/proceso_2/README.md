# Proceso 2

## Proyecto y Propuesta

El objetivo de este proyecto es desarrollar un creador y entrenador de modelos que pueda manejar datos históricos y realizar predicciones basadas en ventanas de datos de tamaño variable. El sistema debe ser capaz de entrenar modelos que puedan predecir el comportamiento del precio en un lapso de tiempo equivalente al 30% del ancho de la ventana de entrada.

## Gestión de Bloques

### Adquisición de Datos

El bloque de adquisición de datos se encargará de recuperar los archivos de datos históricos desde un directorio específico. Este bloque incluirá módulos para la obtención inicial, almacenamiento, preparación final, transformación y validación de los datos.

#### Módulos de Adquisición de Datos

- **Obtención Inicial**: Conector, extractor, gestor de errores, parser, validador.
- **Almacenamiento**: Cache, compressor, gestor de archivos, indexador, versionador.
- **Preparación Final**: Balanceador, constructor de matrices, empaquetador, escalador, generador de ventanas.
- **Transformación**: Agregador, convertidor, enriquecedor, filtro, procesador.
- **Validación**: Analizador de datos, detector de anomalías, gestor de calidad, normalizador, verificador de estructura, gestor de sesiones.

### Controladores Globales

El bloque de controladores globales gestionará la configuración, integración, monitorización, recursos y seguridad del sistema. Este bloque asegurará que todos los componentes del sistema funcionen de manera coordinada y eficiente.

#### Módulos de Controladores Globales

- **Configuración**: Cache, gestor de parámetros, parser, serializador, validador de configuración.
- **Integración**: Broker, comunicador, gestor de eventos, sincronizador, validador.
- **Monitorización**: Alertas, analizador, dashboard, logger, recolector de métricas.
- **Recursos**: Gestor de CPU, gestor de GPU, gestor de memoria, gestor de red, optimizador.
- **Seguridad**: Auditor, autenticador, encriptador, gestor de permisos, recuperador, gestor de sesiones.

### Núcleo Sináptico

El núcleo sináptico será responsable de la construcción del modelo, entrenamiento, validación, optimización e inferencia. Este bloque incluirá módulos para arquitecto de red, gestor de capas, configurador de red, constructor de bloques, validador de arquitectura, entre otros.

#### Módulos del Núcleo Sináptico

- **Construcción del Modelo**: Arquitecto de red, gestor de capas, configurador de red, constructor de bloques, validador de arquitectura.
- **Entrenamiento**: Gestor de entrenamiento, optimizador de pesos, monitor de entrenamiento, gestor de lotes, checkpoint manager.
- **Validación**: Evaluador de modelo, métricas especializadas, generador de reportes, validador cruzado, analizador de resultados, analizador de datos.
- **Optimización**: Ajuste de hiperparámetros, selector de arquitectura, optimizador de rendimiento, buscador de topología, evaluador de configuraciones.
- **Inferencia**: Motor de predicción, gestor de batch, pipeline de inferencia, cache de predicciones, monitor de rendimiento.

## Proceso de Aprendizaje

### Configuración

El archivo `configuracion.json` debe incluir todas las configuraciones necesarias para los componentes que se van a utilizar. Esto incluye rutas a los subdirectorios `modelos` y `checkpoints`, así como parámetros específicos para cada módulo.

### Ejemplo de Configuración

```json
{
    "ruta_datos": "C:\\Users\\jeron\\Documents\\MODELS\\MOD7\\datos\\forex",
    "ruta_modelo": "C:\\Users\\jeron\\Documents\\MODELS\\MOD7\\Proyecto\\composiciones\\proceso_2\\modelos",
    "ruta_checkpoints": "C:\\Users\\jeron\\Documents\\MODELS\\MOD7\\Proyecto\\composiciones\\proceso_2\\checkpoints",
    "ruta_predicciones": "C:\\Users\\jeron\\Documents\\MODELS\\MOD7\\Proyecto\\composiciones\\proceso_2\\predicciones.txt",
    "ventana": 100,
    "parametros_entrenamiento": {
        "epochs": 50,
        "batch_size": 32,
        "learning_rate": 0.001
    }
}
```

### Proceso de Entrenamiento

1. **Cargar Configuración**: Cargar la configuración desde el archivo `configuracion.json`.
2. **Crear Directorios**: Crear los directorios necesarios para almacenar los modelos y checkpoints.
3. **Obtener Datos Normalizados**: Recuperar y normalizar los datos históricos desde el directorio especificado.
4. **Entrenar el Modelo**: Utilizar los datos normalizados para entrenar el modelo.
5. **Guardar el Modelo**: Almacenar el modelo entrenado en el directorio correspondiente.
6. **Realizar Predicciones**: Ingresar una ventana de datos como entrada y obtener predicciones del modelo.

### Validaciones

- **Validación Cruzada**: Utilizar validación cruzada para evaluar el rendimiento del modelo.
- **Métricas Especializadas**: Calcular métricas especializadas para evaluar la precisión y el rendimiento del modelo.
- **Generación de Reportes**: Generar reportes detallados sobre el rendimiento del modelo.

### Ejemplo de Proceso

```python
# main.py
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
    ventana = configuracion['ventana']  # Tamaño de la ventana de datos históricos
    predicciones = predecir(modelo, datos_normalizados, ventana)
    print(predicciones)
    
    # Guardar predicciones
    ruta_predicciones = configuracion['ruta_predicciones']
    guardar_predicciones(predicciones, ruta_predicciones)

if __name__ == '__main__':
    main()
```

## Diagramas de Flujo Secuencial de Procesos

### Diagrama de Flujo del Proceso de Entrenamiento

```plaintext
+---------------------+
| Cargar Configuración|
+---------+-----------+
          |
          v
+---------+-----------+
| Crear Directorios   |
+---------+-----------+
          |
          v
+---------+-----------+
| Obtener Datos       |
| Normalizados        |
+---------+-----------+
          |
          v
+---------+-----------+
| Entrenar Modelo     |
+---------+-----------+
          |
          v
+---------+-----------+
| Guardar Modelo      |
+---------+-----------+
          |
          v
+---------+-----------+
| Realizar Predicciones|
+---------+-----------+
          |
          v
+---------+-----------+
| Guardar Predicciones|
+---------------------+
```

### Diagrama de Flujo del Proceso de Validación

```plaintext
+---------------------+
| Cargar Configuración|
+---------+-----------+
          |
          v
+---------+-----------+
| Crear Directorios   |
+---------+-----------+
          |
          v
+---------+-----------+
| Obtener Datos       |
| Normalizados        |
+---------+-----------+
          |
          v
+---------+-----------+
| Validación Cruzada  |
+---------+-----------+
          |
          v
+---------+-----------+
| Calcular Métricas   |
| Especializadas      |
+---------+-----------+
          |
          v
+---------+-----------+
| Generar Reportes    |
+---------------------+
```

### Lógica para el Bloque Núcleo Sináptico

#### Construcción del Modelo

- **Arquitecto de Red**: Define la arquitectura de la red neuronal.
- **Gestor de Capas**: Gestiona las capas de la red neuronal.
- **Configurador de Red**: Configura los parámetros de la red neuronal.
- **Constructor de Bloques**: Construye los bloques de la red neuronal.
- **Validador de Arquitectura**: Valida la arquitectura de la red neuronal.

#### Entrenamiento

- **Gestor de Entrenamiento**: Gestiona el proceso de entrenamiento.
- **Optimizador de Pesos**: Optimiza los pesos de la red neuronal.
- **Monitor de Entrenamiento**: Monitorea el proceso de entrenamiento.
- **Gestor de Lotes**: Gestiona los lotes de datos para el entrenamiento.
- **Checkpoint Manager**: Gestiona los checkpoints durante el entrenamiento.

#### Validación

- **Evaluador de Modelo**: Evalúa el rendimiento del modelo.
- **Métricas Especializadas**: Calcula métricas especializadas para evaluar el modelo.
- **Generador de Reportes**: Genera reportes detallados sobre el rendimiento del modelo.
- **Validador Cruzado**: Realiza validación cruzada del modelo.
- **Analizador de Resultados**: Analiza los resultados del modelo.
- **Analizador de Datos**: Analiza los datos utilizados para el entrenamiento y validación.

#### Optimización

- **Ajuste de Hiperparámetros**: Ajusta los hiperparámetros del modelo.
- **Selector de Arquitectura**: Selecciona la mejor arquitectura para el modelo.
- **Optimizador de Rendimiento**: Optimiza el rendimiento del modelo.
- **Buscador de Topología**: Busca la mejor topología para el modelo.
- **Evaluador de Configuraciones**: Evalúa diferentes configuraciones del modelo.

#### Inferencia

- **Motor de Predicción**: Realiza predicciones utilizando el modelo entrenado.
- **Gestor de Batch**: Gestiona los lotes de datos para la inferencia.
- **Pipeline de Inferencia**: Gestiona el pipeline de inferencia.
- **Cache de Predicciones**: Almacena las predicciones realizadas.
- **Monitor de Rendimiento**: Monitorea el rendimiento del modelo durante la inferencia.

Esta estructura y metodología permitirán gestionar y ejecutar diferentes flujos de trabajo o procesos de manera organizada y eficiente, con la capacidad de agregar nuevas funciones o componentes según sea necesario.
