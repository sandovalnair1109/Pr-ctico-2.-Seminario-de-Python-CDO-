# TP2 - Python para Ciencia de Datos

Trabajo práctico 2 de la materia **Seminario de Python para Ciencia de Datos** - Licenciatura en Ciencia de Datos, UNLP.

##  Descripción
    Este proyecto contiene 10 ejercicios prácticos que abarcan:
        - Procesamiento y análisis de texto
        - Manipulación de estructuras de datos (listas, diccionarios)
        - Validaciones y normalización de datos

##  Requisitos

- Python 3.10 o superior
- Jupyter Notebook
- Git (para clonar el repositorio)

##  Instalación y ejecución

### Opción 1: Clonar desde GitHub

```bash
git clone https://github.com/sandovalnair1109/Pr-ctico-2.-Seminario-de-Python-CDO-.git
cd Practico_2
```

### Opción 2: Descargar manualmente
    Descargar el ZIP desde GitHub y extraer en la carpeta deseada

## Instalar dependencias
    pip install notebook

## Ejecutar:
    jupyter notebook
    Navegar a notebooks/ y abrir el archivo .ipynb

## Estructura
    Practico_2/
    ├── README.md             
    ├── .gitignore             # Archivos excluidos de Git
    ├── src/                   # Funciones auxiliares
    │   ├── __init__.py
    │   └── funciones_auxiliares.py
    └── notebooks/             # Ejercicios resueltos
        ├── ejercicio1.ipynb   # Estadísticas de texto
        ├── ejercicio2.ipynb   # Duración de playlist
        ├── ejercicio3.ipynb   # Filtro de spoilers
        ├── ejercicio4.ipynb   # Validación de email
        ├── ejercicio5.ipynb   # Calculadora de envío
        ├── ejercicio6.ipynb   # Análisis de hashtags
        ├── ejercicio7.ipynb   # Sorteo amigo invisible
        ├── ejercicio8.ipynb   # Cifrado César
        ├── ejercicio9.ipynb   # Normalización de alumnos
        └── ejercicio10.ipynb  # Competencia de cocina

    Ejercicios inlcuidos
        1. Estadísticas de texto:
            split(), splitlines(), len(), List comprehension para filtrar líneas por encima del promedio
        2. Duración de playlist: 
            split(":"), conversión de formatos, Búsqueda de máximo/mínimo con float('inf')
        3. Filtro de spoilers:
            re.compile(), re.IGNORECASE, re.sub(), Dictionary comprehension {tag: count for ...}
        4. Validación de email:
            count(), split('@'), Validaciones encadenadas con if, Slicing de strings email[0], email[-1]
        5. Calculadora de costo de envío:
        Diccionario anidado para tabla de precios, Acceso por claves precios[zona][rango]
        6. Análisis de hashtags:
            re.findall(), Counter, List comprehension, Lambda en sorted(): key=lambda x: x[1]
        7. Sorteo de amigo invisible:
            random.shuffle(), all() con generador, Validación de duplicados con set()
        8. Cifrado César:
        ord(), chr(), Operador módulo % para rotación, Preservación de mayúsculas/minúsculas
        9. Normalización de registros de alumnos:
            str.title(), str.strip(), Manejo de duplicados con diccionario, Try-except para validar números
        10. Competencia de cocina (OBLIGATORIO):
            enumerate(), Acumulación en diccionario anidado, Lambda en sort(): key=lambda x: x['total'], zip() para emparejar datos


# Video de demostración
    https://drive.google.com/file/d/14eZli1H2qbonLn0mBvKkIQCWRtwQH83G/view?usp=sharing


# Autor
    Alumno/a: Sandoval Nair
    Legajo: 018769/6
    Fecha: Marzo-Abril 2026
    Datos de contacto: sandovalnair368@gmail.com

