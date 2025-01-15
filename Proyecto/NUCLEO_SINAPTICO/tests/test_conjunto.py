import numpy as np
from NUCLEO_SINAPTICO.entrenamiento import entrenar_modelo
from NUCLEO_SINAPTICO.inferencia import predecir

def test_modulo_nucleo_sinaptico():
    X = np.array([[1, 2]])
    y = np.array([1])
    configuracion = {'epochs': 10, 'learning_rate': 0.01}
    modelo = entrenar_modelo(X, y, configuracion)
    assert modelo is not None, "Error en el módulo de entrenamiento"

    predicciones = predecir(modelo, X)
    assert predicciones is not None, "Error en el módulo de inferencia"

    print("Pruebas del módulo NUCLEO_SINAPTICO pasadas")

if __name__ == '__main__':
    test_modulo_nucleo_sinaptico()
