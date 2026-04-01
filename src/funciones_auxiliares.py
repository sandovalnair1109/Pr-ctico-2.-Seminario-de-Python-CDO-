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

    print (duration_to_seconds("5:55"))


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