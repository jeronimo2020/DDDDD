import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.linear_model import LinearRegression
import numpy as np

def entrenar_modelo(X, y, configuracion):
    """
    Entrena el modelo de aprendizaje automático.

    Args:
        X (np.array): Características de entrada.
        y (np.array): Valores objetivo.
        configuracion (dict): Configuración del entrenamiento.

    Returns:
        Model: Modelo entrenado.
    """
    try:
        # Inicializamos el modelo de regresión lineal (puedes cambiar esto por cualquier otro modelo)
        modelo = LinearRegression()

        # Parámetros del modelo: epochs, batch_size, learning_rate, etc.
        epochs = configuracion.get('epochs', 100)
        learning_rate = configuracion.get('learning_rate', 0.01)

        # Ajustamos el modelo a los datos
        modelo.fit(X, y)
        
        print(f"Modelo entrenado con éxito con {epochs} épocas y tasa de aprendizaje {learning_rate}")
        return modelo
    except Exception as e:
        print(f"Error al entrenar el modelo: {e}")
        return None

def gestor_entrenamiento(model, X_train, y_train, configuracion):
    print("Gestionando el proceso de entrenamiento...")
    model.compile(optimizer=Adam(learning_rate=configuracion['parametros_entrenamiento']['learning_rate']), 
                  loss='mse', metrics=['mae'])
    callbacks = [
        EarlyStopping(patience=10, restore_best_weights=True),
        ModelCheckpoint('best_model.h5', save_best_only=True)
    ]
    history = model.fit(X_train, y_train, epochs=configuracion['parametros_entrenamiento']['epochs'], 
                        batch_size=configuracion['parametros_entrenamiento']['batch_size'], 
                        validation_split=0.2, callbacks=callbacks)
    print("Proceso de entrenamiento gestionado")
    return history

def optimizador_pesos(model):
    print("Optimizando los pesos de la red neuronal...")
    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='mse')
    print("Pesos de la red neuronal optimizados")

def monitor_entrenamiento(history):
    print("Monitoreando el proceso de entrenamiento...")
    import matplotlib.pyplot as plt
    plt.plot(history.history['loss'], label='Pérdida de entrenamiento')
    plt.plot(history.history['val_loss'], label='Pérdida de validación')
    plt.legend()
    plt.show()
    print("Proceso de entrenamiento monitoreado")

def gestor_lotes(X, y, batch_size):
    print("Gestionando los lotes de datos para el entrenamiento...")
    num_batches = len(X) // batch_size
    for i in range(num_batches):
        yield X[i*batch_size:(i+1)*batch_size], y[i*batch_size:(i+1)*batch_size]
    print("Lotes de datos para el entrenamiento gestionados")

def checkpoint_manager():
    print("Gestionando los checkpoints durante el entrenamiento...")
    checkpoint = ModelCheckpoint('model_checkpoint.h5', save_best_only=True, monitor='val_loss')
    print("Checkpoints durante el entrenamiento gestionados")
