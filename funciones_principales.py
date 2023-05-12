from importe_archivos import *
#2
def contar_por_raza(lista:list)->dict:
    '''
    Brief: Recibe una lista de diccionarios que representan personajes y una clave específica. cuenta cuántas veces aparece cada valor de la característica en la lista y devolver un diccionario que muestre esos conteos.
    Parameters:
        lista: str ->  Una lista de diccionarios con la informacion de los personajes
        clave:str -> La característica específica que quieres contar en los personajes
    Return: Un diccionario que muestra el recuento de cada valor de la característica
    '''
    diccionario_caracteristicas = {}
    for personaje in lista:
        if personaje['race'] in diccionario_caracteristicas:
            diccionario_caracteristicas[personaje['race']] += 1
        else:
            diccionario_caracteristicas[personaje['race']] = 1 
    for raza, cantidad in diccionario_caracteristicas.items():
        print(f"Raza: {raza}")
        print(f"cantidad de personajes: {cantidad}")

# 3
def listar_agrupados(lista:list, clave:str)->None:
    '''
    Brief: Agrupar los personajes según el valor de la clave proporcionada y mostrarlos en una lista organizada.
    Parameters:
        lista: str -> Una lista de diccionarios con la informacion de los personajes
        clave:str -> a clave específica utilizada para agrupar los personajes
    Return: Un diccionario que muestra el recuento de cada valor de la característica
    '''
    lista_agrupados = []
    for personaje in lista:
        heroes = personaje[clave]
        lista_agrupados.append(heroes)
    lista_agrupados_sin_repetidos = set(lista_agrupados)
    for atributo in lista_agrupados_sin_repetidos:
        print(atributo + ":")
        for personaje in lista:
            if personaje[clave] == atributo:
                print(f"# Nombre: {personaje['name']} - Poder de ataque: {personaje['attack_power']}")
# 4
def buscar_personajes_por_habilidad(lista:list):
    '''
    Brief: Agrupa a los personajes segun sus habilidades, ademas muestra los nombres, la raza y el promedio de atque y defensa
    Parameters:
        lista: str -> La lista donde va a buscar a los personajes para luego agruparlos
    Return: None
    '''
    habilidad_usario = validacion_ingresos(lista, 'ability', 'una habilidad: ')
    print(f"{habilidad_usario}:")
    for personaje in lista:
        promedio = (personaje['attack_power'] + personaje['fight_power']) / 2
        if habilidad_usario == personaje['ability']:
            print(f"Nombre: {personaje['name']} - Raza: {personaje['race']} - Promedio: {promedio}")
            
#buscar_personajes_por_habilidad(lista_ajustada_habilidad)
