"""
Funciones auxiliares para los ejercicios del TP2
"""
import re

def duration_to_seconds(duration_str):
    #le paso como parámetro la duración de cada canción
    """
    Convierte string "m:ss" a segundos totales.
    Ejemplo: "5:55" --> 5*60 +55 = 355 segundos
    """

    minutes, second = duration_str.split(":") 
    return int(minutes)*60 + int(second) #devuelve el formato que se pide

def reemplazar_ignore_case(texto, objetivo, reemplazo):
    """ 
    Reemplaza 'objetivo' por 'reemplazo' en 'texto'
    """
    import re
    #re.IGNORECASE hace que no importe si es mayus/minus
    #re.escape ignora los caracteres especiales
    patron= re.compile (re.escape(objetivo),re.IGNORECASE)
    #sustituimos con .sub()
    return patron.sub(reemplazo, texto)

def censurar_texto(texto, palabras_prohibidas):
    """
    Reemplaza cada palabra prohibida por astericos (*).
    Mantiene el mismo número de caracteres.

    """
    texto_censurado= texto
    for palabra in palabras_prohibidas:
        #nos aseguramos que los asteriscos tengan la misma longitud
        astericos="*" * len(palabra)
        #llamo a la función que reemplaza las palabras por los asteriscos en el texto
        texto_censurado= reemplazar_ignore_case(texto_censurado, palabra, astericos)
        #devuelvo el texto ya censurado
    return texto_censurado

