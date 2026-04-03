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

def validar_email (email):
    """
    Valida una dirección de email según los criterios pedidos.
    Returna True si es válido, False si no
    """

    #Criterio 1: Solo un @
    if email.count('@') != 1:
        return False
    #separamos en parte local y dominio
    parte_local, dominio= email.split('@')

    #Criterio 2: al menos 1 carácter antes del @
    if len(parte_local) == 0:
        return False
    
    #Criterio 4: no empieza con @ ni con un punto
    if email[0] == '@' or email[0] == '.':
        return False
    #Criterio 4: no termina con @ ni con un punto
    if email[-1] == '@' or email[-1] == '.':
        return False

    #Criterio 3: al menos un punto después del @ (en el dominio)
    if '.' not in dominio:
        return False
    
    #Criterio 5: desdepués del último punto, al menos 2 caracteres
    extension= dominio.split('.')[-1]
    if len(extension) < 2:
        return False
    
    #Si pasó todos los criterios
    return False

def calcular_costo_envio(peso, zona):
    """
    Calcula el costo de envío según peso y zona.
    Parámetros:
        peso:número en kg
        zona:string 'local', 'regional' o 'nacional'
    Retorna:
        costo (int) si la zona es válida
        None si la zona no lo es
    """
    #verificamos si la zona es válida
    zonas_validas = ['local', 'regional','nacional']
    if zona.lower() not in zonas_validas:
        return None
    
    #determinar rango de peso
    if peso <= 1:
        rango= 'hasta_1kg'
    elif peso <= 5:
        rango= '1_a_5kg'
    else:
        rango= 'mas_de_5kg'
    
    #tabla de precios
    precios= {
        'local':{'hasta_1kg':500 , '1_a_5kg':1000, 'mas_de_5kg':2000},
        'regional':{'hasta_1kg':1000 , '1_a_5kg':2500, 'mas_de_5kg':5000},
        'nacional':{'hasta_1kg':2000 , '1_a_5kg':4500, 'mas_de_5kg':8000}
    }
    #accedo primero a la zona si correcta, y luego al rango (diccionario dentro de diccionario)
    return precios[zona.lower()][rango]

