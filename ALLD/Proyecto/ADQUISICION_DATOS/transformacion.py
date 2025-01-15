# Aquí puedes implementar funciones adicionales para la transformación de los datos
# como agregación, conversión, enriquecimiento, filtrado y procesamiento.

def agregador(datos):
    print("Agregando datos...")
    try:
        total = sum(dato['valor'] for dato in datos)
        print("Datos agregados")
        return total
    except Exception as e:
        print(f"Error al agregar datos: {e}")
        return 0

def convertidor(datos):
    print("Convirtiendo datos...")
    try:
        datos_convertidos = [{'fecha': dato['fecha'], 'valor': str(dato['valor'])} for dato in datos]
        print("Datos convertidos")
        return datos_convertidos
    except Exception as e:
        print(f"Error al convertir datos: {e}")
        return []

def enriquecedor(datos):
    print("Enriqueciendo datos...")
    try:
        datos_enriquecidos = [{'fecha': dato['fecha'], 'valor': dato['valor'], 'enriquecido': True} for dato in datos]
        print("Datos enriquecidos")
        return datos_enriquecidos
    except Exception as e:
        print(f"Error al enriquecer datos: {e}")
        return []

def filtro(datos, umbral):
    print("Filtrando datos...")
    try:
        datos_filtrados = [dato for dato in datos if dato['valor'] > umbral]
        print("Datos filtrados")
        return datos_filtrados
    except Exception as e:
        print(f"Error al filtrar datos: {e}")
        return []

def procesador(datos):
    print("Procesando datos...")
    try:
        datos_procesados = [{'fecha': dato['fecha'], 'valor': dato['valor'] * 2} for dato in datos]
        print("Datos procesados")
        return datos_procesados
    except Exception as e:
        print(f"Error al procesar datos: {e}")
        return []
