from ADQUISICION_DATOS.obtencion_inicial import obtener_datos_normalizados
from ADQUISICION_DATOS.preparacion_final import balanceador, constructor_matrices, empaquetador, escalador, generador_ventanas
import numpy as np

def test_modulo_adquisicion_datos():
    ruta = 'ruta_a_tu_archivo.csv'
    datos_normalizados = obtener_datos_normalizados(ruta)
    assert datos_normalizados is not None, "Error en el módulo de obtención inicial"

    datos = [{'clase': 1, 'valor': 10}, {'clase': 0, 'valor': 5}]
    datos_balanceados = balanceador(datos)
    assert datos_balanceados is not None, "Error en el módulo de preparación final - balanceador"

    datos = [[1, 2], [3, 4]]
    matrices = constructor_matrices(datos)
    assert matrices is not None, "Error en el módulo de preparación final - constructor_matrices"

    datos = [{'fecha': '2023-01-01', 'valor': 10}]
    datos_empaquetados = empaquetador(datos)
    assert datos_empaquetados is not None, "Error en el módulo de preparación final - empaquetador"

    datos = np.array([[1, 2], [3, 4]])
    datos_escalados = escalador(datos)
    assert datos_escalados is not None, "Error en el módulo de preparación final - escalador"

    datos = [1, 2, 3, 4, 5]
    ventana = 2
    ventanas = generador_ventanas(datos, ventana)
    assert ventanas is not None, "Error en el módulo de preparación final - generador_ventanas"

    print("Pruebas del módulo ADQUISICION_DATOS pasadas")

if __name__ == '__main__':
    test_modulo_adquisicion_datos()
