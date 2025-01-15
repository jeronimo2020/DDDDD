from CONTROLADORES_GLOBALES.configuracion import cargar_configuracion

def test_modulo_controladores_globales():
    ruta_config = 'configuracion.json'
    configuracion = cargar_configuracion(ruta_config)
    assert configuracion is not None, "Error en el módulo de configuración"

    print("Pruebas del módulo CONTROLADORES_GLOBALES pasadas")

if __name__ == '__main__':
    test_modulo_controladores_globales()
