# Guía Técnica para el Entrenamiento de Modelos Financieros

## Introducción
Este documento tiene como objetivo proporcionar una guía clara y estructurada para entrenar un modelo de predicción financiera basado en datos históricos de pares de divisas. El enfoque está orientado hacia el uso de arquitecturas híbridas que combinen Redes Neuronales Densas (DNN) y Redes Neuronales Recurrentes (RNN), aprovechando así lo mejor de ambos enfoques para detectar patrones temporales y relaciones complejas en los datos.

## Requerimientos Previos

1. **Datos**: Datos históricos de alta calidad con:
   - Fechas y tiempos consistentes.
   - Indicadores técnicos calculados previamente (e.g., RSI, MACD, medias móviles).
   - Etiquetas claras para predicción si aplica (e.g., dirección del precio, magnitud del cambio).

2. **Entorno**: Un entorno bien configurado que incluya:
   - Lenguaje Python.
   - Bibliotecas: TensorFlow, Keras, Pandas, NumPy, Scikit-learn.
   - Recursos computacionales adecuados (CPU/GPU).

3. **Preprocesamiento**: Asegúrate de que los datos han sido:
   - Normalizados o estandarizados.
   - Divididos en ventanas de tiempo.
   - Limpios de valores atípicos extremos y vacíos.

---

## Estrategia de Entrenamiento

### 1. División de Datos

1. **División temporal**:
   - Divide los datos en:
     - **Entrenamiento**: ~70% de los datos.
     - **Validación**: ~20% de los datos.
     - **Prueba**: ~10% de los datos.
   - Garantiza que las divisiones sean consecutivas en el tiempo.

2. **Ventanas deslizantes**:
   - Crea ventanas deslizantes de datos para capturar patrones temporales:
     - **Ventana de entrada (X)**: Un rango de tiempo (e.g., 30 días).
     - **Ventana de salida (Y)**: El valor objetivo que se predice (e.g., precio de cierre en los próximos 5 días).

### 2. Arquitectura del Modelo

1. **Componente DNN**:
   - Diseñado para identificar relaciones complejas entre los indicadores técnicos.
   - Ejemplo de arquitectura:
     ```python
     from tensorflow.keras.layers import Dense, Dropout
     dense_part = Sequential([
         Dense(128, activation='relu', input_shape=(n_features,)),
         Dropout(0.2),
         Dense(64, activation='relu')
     ])
     ```

2. **Componente RNN**:
   - Diseñado para capturar patrones temporales en los datos.
   - Usa capas LSTM o GRU:
     ```python
     from tensorflow.keras.layers import LSTM
     rnn_part = Sequential([
         LSTM(64, return_sequences=True, input_shape=(time_steps, n_features)),
         LSTM(32)
     ])
     ```

3. **Combinación**:
   - Fusiona las salidas de DNN y RNN para una predicción final.
     ```python
     from tensorflow.keras.layers import Concatenate
     combined = Concatenate()([dense_part.output, rnn_part.output])
     final_output = Dense(1, activation='linear')(combined)
     ```

### 3. Configuración del Entrenamiento

1. **Pérdida y Optimizador**:
   - Pérdida: MSE (Error cuadrático medio) para regresión o Categorical Crossentropy para clasificación.
   - Optimizador: Adam con tasa de aprendizaje ajustable.
     ```python
     from tensorflow.keras.optimizers import Adam
     model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
     ```

2. **Callbacks**:
   - EarlyStopping: Detener el entrenamiento si no hay mejora en la pérdida de validación.
   - ModelCheckpoint: Guardar el mejor modelo basado en validación.
     ```python
     from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
     callbacks = [
         EarlyStopping(patience=10, restore_best_weights=True),
         ModelCheckpoint('best_model.h5', save_best_only=True)
     ]
     ```

### 4. Validación y Evaluación

1. **Validación Cruzada Temporal**:
   - Divide el conjunto de entrenamiento en varias partes temporales (folds) para validar en diferentes intervalos de tiempo.

2. **Métricas**:
   - Regresión: MAE, RMSE.
   - Clasificación: Precisión, F1 Score.

3. **Gráficas**:
   - Compara las predicciones del modelo con los valores reales para identificar patrones incorrectos.

### 5. Inferencia y Ajustes

1. **Pipeline de Inferencia**:
   - Procesa datos en tiempo real aplicando las mismas transformaciones que en el entrenamiento.
   - Realiza predicciones por lotes para mejorar el rendimiento.

2. **Técnicas Avanzadas**:
   - **Transfer Learning**: Usa modelos preentrenados como punto de partida.
   - **Ensemble Models**: Combina múltiples modelos para mejorar la robustez de las predicciones.

---

## Procedimiento Resumido

1. **Preprocesa los datos**:
   - Limpia, normaliza y crea ventanas deslizantes.
2. **Define y construye el modelo**:
   - Crea una arquitectura híbrida que combine DNN y RNN.
3. **Entrena el modelo**:
   - Utiliza estrategias como EarlyStopping y Callbacks.
4. **Valida y evalúa**:
   - Aplica validación cruzada temporal y métricas relevantes.
5. **Ajusta y optimiza**:
   - Realiza ajustes iterativos basados en el rendimiento.
6. **Implementa la inferencia**:
   - Configura un pipeline para procesar datos en tiempo real.

---

## Conclusión
Este documento proporciona una guía paso a paso para entrenar y evaluar un modelo financiero. Sigue estas instrucciones para garantizar que el modelo sea robusto, preciso y eficiente.
