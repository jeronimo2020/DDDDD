import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import numpy as np
from NUCLEO_SINAPTICO.entrenamiento import entrenar_modelo
from NUCLEO_SINAPTICO.inferencia import predecir

def test_entrenar_modelo():
    X = np.array([[1, 2], [3, 4]])
    y = np.array([1, 0])
    configuracion = {'epochs': 10, 'learning_rate': 0.01}
    modelo = entrenar_modelo(X, y, configuracion)
    assert modelo is not None, "Error al entrenar el modelo"
    print("Prueba de entrenar_modelo pasada")

def test_predecir():
    X = np.array([[1, 2], [3, 4]])
    y = np.array([1, 0])
    configuracion = {'epochs': 10, 'learning_rate': 0.01}
    modelo = entrenar_modelo(X, y, configuracion)
    predicciones = predecir(modelo, X)
    assert predicciones is not None, "Error al realizar predicciones"
    print("Prueba de predecir pasada")

if __name__ == '__main__':
    test_entrenar_modelo()
    test_predecir()
