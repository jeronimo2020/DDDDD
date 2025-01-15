import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from ADQUISICION_DATOS.obtencion_inicial import obtener_datos_normalizados
from ADQUISICION_DATOS.preparacion_final import balanceador, constructor_matrices, empaquetador, escalador, generador_ventanas
import numpy as np

def test_obtener_datos_normalizados():
    ruta = 'ruta_a_tu_archivo.csv'
    datos_normalizados = obtener_datos_normalizados(ruta)
    assert datos_normalizados is not None, "Error al obtener los datos normalizados"
    print("Prueba de obtener_datos_normalizados pasada")

def test_balanceador():
    datos = [{'clase': 1, 'valor': 10}, {'clase': 0, 'valor': 5}]
    datos_balanceados = balanceador(datos)
    assert datos_balanceados is not None, "Error al balancear los datos"
    print("Prueba de balanceador pasada")

def test_constructor_matrices():
    datos = [[1, 2], [3, 4]]
    matrices = constructor_matrices(datos)
    assert matrices is not None, "Error al construir las matrices"
    print("Prueba de constructor_matrices pasada")

def test_empaquetador():
    datos = [{'fecha': '2023-01-01', 'valor': 10}]
    datos_empaquetados = empaquetador(datos)
    assert datos_empaquetados is not None, "Error al empaquetar los datos"
    print("Prueba de empaquetador pasada")

def test_escalador():
    datos = np.array([[1, 2], [3, 4]])
    datos_escalados = escalador(datos)
    assert datos_escalados is not None, "Error al escalar los datos"
    print("Prueba de escalador pasada")

def test_generador_ventanas():
    datos = [1, 2, 3, 4, 5]
    ventana = 2
    ventanas = generador_ventanas(datos, ventana)
    assert ventanas is not None, "Error al generar las ventanas de datos"
    print("Prueba de generador_ventanas pasada")

if __name__ == '__main__':
    test_obtener_datos_normalizados()
    test_balanceador()
    test_constructor_matrices()
    test_empaquetador()
    test_escalador()
    test_generador_ventanas()
