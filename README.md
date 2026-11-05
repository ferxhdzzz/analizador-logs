# Analizador de Archivos Log en Python

**Estudiante:** Fernanda Hernandez

**Institución:** Kodigo 

**Materia:** Análisis de Logs y Desarrollo de Software  

**Lenguaje:** Python  

---

## Descripción del Proyecto

Este proyecto consiste en un script de consola desarrollado en Python diseñado para procesar y analizar archivos de registros (`logs`)
de aplicaciones informáticas. El sistema examina línea por línea el archivo seleccionado, extrae y 
clasifica los eventos según su nivel de severidad (`INFO`, `WARNING`, `ERROR`), valida la precisión de 
los sellos de tiempo en formato ISO (`AAAA-MM-DD`) y detecta anomalías o líneas mal formateadas.

---

## Características Principales

- **Selección dinámica de archivos:** Permite ingresar rutas absolutas o relativas al ejecutar el programa.
- **Validación sintáctica mediante Regex:** Expresión regular flexible que soporta viñetas (`·`), guiones y corchetes opcionales alrededor del nivel de severidad.
- **Validación lógica de fechas:** Verifica con la librería nativa `datetime` la validez real de la fecha en el calendario (detectando fechas imposibles como `2025-02-31`).
- **Control de errores e inconsistencias:** Maneja excepciones de archivos no encontrados (`FileNotFoundError`) e identifica líneas corruptas o niveles no reconocidos.
- **Reporte resumido en consola:** Muestra métricas claras sobre total de eventos, distribución por severidad y calidad de datos.

---

## Estructura del Proyecto

```text
/proyecto-log-analyzer
│
├── analizador_logs.py        # Script principal en Python
├── log_correcto.txt          # Archivo de prueba (Caso de éxito / Ideal)
├── log_inconsistente.txt     # Archivo de prueba (Caso con errores y casos borde)
└── README.md                 # Documentación del proyecto y reporte técnico
