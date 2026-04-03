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

from collections import Counter
def extraer_hashtags (texto):
    """
    Extrae todos los hashtags (#palabra) de un texto.
    Retorna una lista de hashtags encontrados
    """
    #\w+ busca letras, números y guiones bajos
    #El patrón busca # seguido de caracteres de palabra/s
    return re.findall (r'#\w+', texto)

def analizar_hashtags (posts):
    """"
    Analiza una lista de post y retorna estadísiticas de hashtags.
    Retorna:
        -trending: dict con hashtags que aparecen >1 vez
        -total_unicos: int con cantidad total de hashtags únicos
        -todos_los_hashtags: lista completa para referencia
    """
    todos_los_hashtags=[]

    #extraer hashtags de cada post
    for post in posts:
        hashtags= extraer_hashtags(post)
        #guarda cada hashtag de cada post en una lista
        todos_los_hashtags.extend(hashtags)
    
    #contador frecuencias, automáticamente agrupa por clave única
    contador= Counter(todos_los_hashtags)

    #filtrar trending (más de 1 aparición) --> "Arma un diccionario donde cada elemento sea el hashtag y cuántas veces aparece, 
    # recorriendo cada hashtag y cantidad, pero solo si la cant es mayor a uno"
    trending = {tag:count for tag, count in contador.items() if count > 1}

    total_unicos= len(contador)

    return trending, total_unicos,contador



import random
def validar_participantes (nombres):
    """
    Validar que haya al menos 3 participantes y no haya duplicados
    retorna (True, lista_limpia) o (Flase, mensaje_error)
    """
    #limpiar espacios
    limpios = [nombre.strip() for nombre in nombres]

    #nos aseguramos que la cantidad sea suficiente
    if len(limpios)<3:
        return False, "Debe haber al menos 3 participantes"
    
    #nos aseguramos que no hay duplicados
    normalizados = [n.lower() for n in limpios]
    # set() elimina los duplicados automáticamente
    if len(set(normalizados)) != len(normalizados):
        return False, "No debe haber nombres duplicados"
    
    return True, limpios

def sorteo_amigo_invisible (participantes):
    """
    Realiza el sorteo asefurando que nadie se tenga a sí mismo
    Retorna lista de tuplas (quien_regala, quien_recibe)
    """

    #crear copia para mezclar
    destinatarios = participantes.copy()

    #mezclar hasta que nadie coincida con su posición original
    while True:
        random.shuffle(destinatarios)
        #verificar que nadie se tenga a sí mismo
        #devuelve true si para cada pareja (p,d) el que regala no es el mismo que recibe (p!=d), ya que la lista de destinatarios es una copia de la de participantes. Si se cumple, el sorteo es válido
        #zip() une ambas listas en pares
        valido = all(p != d for p, d in zip(participantes, destinatarios))
        if valido:
            break
    return list(zip(participantes, destinatarios))

def cifrar_cesar (texto, desplazamiento):
    """
    Cifra un texto usando el método Cesar.
    Preserva mayúsculas/minúsculas y caracteres no alfabéticos
    """

    resultado= []
    for caracter in texto:
        if caracter.isalpha(): #verifica si la letra es mayúscula
            #determinar si es mayúscula o minúscula
            if caracter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            #Calcular nueva pos con rotación
            #ord() convierte un carácter en su código numérico
            #chr() hace lo contrario: convierte un número en carácter

            #trabajamos con posiciones de 0-25, pregunto el codigo del caracter y le resto la base, para saber la pos, y a este valor le sumamos el desplazamiento
            nueva_pos= (ord(caracter)- base + desplazamiento)%26 #si te pasás de la letra 25 (z), volves a 0 (la A)
            #pasamos nuevamente la pos a caracter
            nuevo_char= chr (base + nueva_pos)
            #lo agrego a la lista
            resultado.append(nuevo_char)
        else:
            #si no es letra (espacio, signo, nro), se mantiene igual
            resultado.append(caracter)
    
    #juntamos los elementos de la lista en un solo texto
    return ''.join(resultado)

    
def descifrar_cesar (mensaje_cifrado, desplazamiento):
    """
    Descifra un mensaje cifrado con César.
    Básicamente aplica el mismo algoritmo pero con desplazaciento negativo.
    Retorna el mensaje original
    """
    return cifrar_cesar(mensaje_cifrado, -desplazamiento)

def limpiar_registros_alumnos(students):
    """
    Limpia y normaliza registros de alumnos.
    Retorna lista de diccionarios limpios y ordenados
    """

    alumnos_limpios={}
    for student in students:
        #paso 1: nos aseguramos que no sea nombre vacío
        nombre = student.get('name')
        if nombre is None or str(nombre).strip() == "":
            continue #Saltar este registro
        nombre = str(nombre).strip()

        #paso2: nos aseguramos que la nota sea numerica y no sea vacía
        nota = student.get('grade')
        if nota is None or str(nota).strip() == "":
            continue

        #Intentar convertir a número
        try:
            nota_num = int(float(str(nota).strip()))
        except ValueError:
            #si no es nro, descartar
            continue
        
        #paso 3:nos aseguramos que el estado no sea vacío
        estado = student.get('status')
        if estado is None:
            estado = "Aprobado" if nota_num >= 4 else "Desaprobado"
        else:
            estado = str(estado).strip()
        
        #paso 4: normalizamos el formato
        nombre_nosrmalizado= nombre.title()
        estado_normalizado= estado.title()

        #paso 5: procesar duplicados
        if nombre_nosrmalizado in alumnos_limpios:
            #si ya existe, quedarse con la nota más alta
            if nota_num > alumnos_limpios[nombre_nosrmalizado]['grade']:alumnos_limpios[nombre_nosrmalizado] = {
                'name':nombre_nosrmalizado,
                'grade':nota_num,
                'status':estado_normalizado
            }
        else:
            #agregar nuevo alumno
            alumnos_limpios[nombre_nosrmalizado] = {
                'name':nombre_nosrmalizado,
                'grade':nota_num,
                'status': estado_normalizado
            }
    #paso 6: convertir diccionario a lista y ordenar alfabéticamente
    lista_final = list(alumnos_limpios.values())
    lista_final.sort(key=lambda x: x['name'])

    return lista_final