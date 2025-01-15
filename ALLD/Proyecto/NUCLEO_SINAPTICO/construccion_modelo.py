from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Dropout, Concatenate

def arquitecto_red(input_shape):
    print("Definiendo la arquitectura de la red neuronal...")
    inputs = Input(shape=input_shape)
    return inputs

def gestor_capas(inputs):
    print("Gestionando las capas de la red neuronal...")
    x = Dense(128, activation='relu')(inputs)
    x = Dropout(0.2)(x)
    x = Dense(64, activation='relu')(x)
    return x

def configurador_red(inputs):
    print("Configurando los parámetros de la red neuronal...")
    x = LSTM(64, return_sequences=True)(inputs)
    x = LSTM(32)(x)
    return x

def constructor_bloques(dense_output, rnn_output):
    print("Construyendo los bloques de la red neuronal...")
    combined = Concatenate()([dense_output, rnn_output])
    final_output = Dense(1, activation='linear')(combined)
    return final_output

def validador_arquitectura(model):
    print("Validando la arquitectura de la red neuronal...")
    model.summary()
    print("Arquitectura de la red neuronal validada")
