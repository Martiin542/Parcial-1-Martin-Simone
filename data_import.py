import re
##1##
def parser_csv(ruta:str)->list:
    '''
    Brief: Recibe la ruta de un archivo CSV y lee su contenido para convertirlo en una lista de diccionarios. Cada diccionario representa un personaje y sus caracteristicas, luego devuelve la lista de personajes.
    Parameters: 
        ruta: str ->  La ruta del archivo CSV sobre la va a analizar y convertir en una lista de personajes
    Return: Una lista de diccionarios, donde cada diccionario representa un personaje con sus atributos
    '''
    with open(ruta, 'r', encoding = "utf-8") as archivo:
        lista = []
        for linea in archivo:
            lectura = re.split(",", linea)
            personaje = {}
            personaje['ID'] = int(lectura[0])
            personaje['nombre'] = lectura[1] 
            personaje['raza'] = lectura[2] 
            personaje['poder_pela'] = int(lectura[3])
            personaje['poder_ataque'] = int(lectura[4])
            personaje['hablidad'] = lectura[5] 
            lista.append(personaje)
    return lista
##spliter##
def split_race(personaje:str)->None:
    '''
    Brief: Divide a las claves 'raza' y 'hablidad'
    Parameters: 
        personaje: str -> El personaje que hay que pasarle dentro del for
    Return: None
    '''
    personaje['raza'] = re.split(r"-(?=[H])", personaje['raza'])
    personaje['hablidad'] = [elemento.strip() for elemento in re.split(r'\|\$\%', personaje['hablidad'])]
##listas por clave##
def listar_por_claves(lista:list, clave:str)->list:
    '''
    Brief: Crea una lista con los valores que hay dentro la clave que le pasemos
    Parameters: 
        lista: list -> La lista de donde sacamos las claves
        clave: str -> Las clave a la cual le vamos a extrar los valores
    Return: list
    '''
    lista_de_claves = []
    for personaje in lista:
        split_race(personaje)
        for caracteristica in personaje[clave]:
            if caracteristica not in lista_de_claves:
                lista_de_claves.append(caracteristica)
    return lista_de_claves
##input##
def validar_input(lista:list, campo:str)->str:
    '''
    Brief: Valida los input que ingresa el usario
    Parameters: 
        lista: list -> La lista de donde vamos a comprar que el input del usario coincida
        campo: str -> Donde queremos comparar (raza o nombre)
    Return: string
    '''
    while True:
        valor = input(f"Ingrese el valor de {campo}: ")
        for elemento in lista:
            if elemento['nombre'] == valor or elemento['raza'] == valor:
                return elemento[campo]
        print("Los valores ingrsados no son validos.")


lista_principal = parser_csv('DBZ.csv')
#print(lista_principal)