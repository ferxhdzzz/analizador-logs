import os
import re
from datetime import datetime

# Regex para extraer: Nivel de severidad, Fecha opcional y el Mensaje restante
# Soporta corchetes [INFO] o palabras directas, y viñetas como '·' al inicio
LOG_PATTERN = re.compile(
    r"^[·\s\-\*]*\[?(INFO|WARNING|ERROR)\]?\s+(?:(\d{4}-\d{2}-\d{2})\s+)?(.+)$",
    re.IGNORECASE
)

def validar_fecha(fecha_str):
    """valida si un texto cumple estrictamente con el formato AAAA-MM-DD y es una fecha real."""
    if not fecha_str:
        return False
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def analizar_archivo_log(ruta_archivo):
    """lee y procesa el archivo de registro aplicando las reglas de validación definidas."""
    resumen = {
        "total_lineas": 0,
        "severidad": {"INFO": 0, "WARNING": 0, "ERROR": 0},
        "fechas_validas": 0,
        "lineas_mal_formateadas": 0
    }

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                if not linea:
                    continue  # Ignorar líneas vacías

                resumen["total_lineas"] += 1
                match = LOG_PATTERN.match(linea)

                if match:
                    severidad = match.group(1).upper()
                    fecha_str = match.group(2)

                    # Contabilizar nivel de severidad
                    resumen["severidad"][severidad] += 1

                    # Validar si la fecha está presente y es válida
                    if validar_fecha(fecha_str):
                        resumen["fechas_validas"] += 1
                    else:
                        # Decisión: Cuenta severidad pero marca falla de formato por fecha
                        resumen["lineas_mal_formateadas"] += 1
                else:
                    # Decisión: Línea no coincide con ninguna severidad válida
                    resumen["lineas_mal_formateadas"] += 1

        return resumen

    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo: '{ruta_archivo}'")
        return None
    except Exception as e:
        print(f"\n[ERROR] Ocurrió un problema inesperado: {e}")
        return None

def mostrar_resumen(resumen, nombre_archivo):
    """imprime los resultados en consola de forma clara y formateada."""
    print("\n" + "="*45)
    print(f" resumen de analisis: {nombre_archivo}")
    print("="*45)
    print(f" total de eventos procesados : {resumen['total_lineas']}")
    print("-" * 45)
    print(" conteo por severidad:")
    print(f"   - [INFO]    : {resumen['severidad']['INFO']}")
    print(f"   - [WARNING] : {resumen['severidad']['WARNING']}")
    print(f"   - [ERROR]   : {resumen['severidad']['ERROR']}")
    print("-" * 45)
    print(" calidad de datos:")
    print(f"   - Eventos con fecha válida     : {resumen['fechas_validas']}")
    print(f"   - Líneas mal formateadas/incompletas: {resumen['lineas_mal_formateadas']}")
    print("="*45 + "\n")

def main():
    print("--- anlizador de archivos de log ---")
    ruta = input("ingresa la ruta del archivo de log a analizar: ").strip()
    
    # Limpiar comillas si el usuario arrastra el archivo a la terminal
    ruta = ruta.strip('"\'')

    if not os.path.exists(ruta):
        print(f"[ERROR] El archivo '{ruta}' no existe. Verifica la ruta.")
        return

    resumen = analizar_archivo_log(ruta)
    if resumen:
        mostrar_resumen(resumen, os.path.basename(ruta))

if __name__ == "__main__":
    main()