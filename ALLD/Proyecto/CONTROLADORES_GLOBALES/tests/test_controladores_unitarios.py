import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from CONTROLADORES_GLOBALES.configuracion import cargar_configuracion

def test_cargar_configuracion():
    ruta_config = 'configuracion.json'
    configuracion = cargar_configuracion(ruta_config)
    assert configuracion is not None, "Error al cargar la configuración"
    print("Prueba de cargar_configuracion pasada")

if __name__ == '__main__':
    test_cargar_configuracion()
