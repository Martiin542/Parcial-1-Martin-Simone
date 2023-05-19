from data_import import *
##2##
def contar_por_raza(lista:list)->None:
    '''
    Brief: Cuenta cuantos personajes hay por cada raza
    Parameters:
        lista: str ->  Una lista de diccionarios con la informacion de los personajes y a que raza pertencen
    Return: None
    '''
    diccionario_caracteristicas = {}
    for personaje in lista:
        split_race(personaje)
        for raza in personaje['raza']:
            if raza in diccionario_caracteristicas:
                diccionario_caracteristicas[raza] += 1
            else:
                diccionario_caracteristicas[raza] = 1 
    for raza, cantidad in diccionario_caracteristicas.items():
        print(f"Raza: {raza}")
        print(f"cantidad de personajes: {cantidad}")
##3##
def listar_personajes_por_raza(lista:list)->None:
    '''
    Brief: Agrupar los personajes según su raza.
    Parameters:
        lista: str -> Una lista de diccionarios con la informacion de los personajes
    Return: None
    '''
    listado_razas = listar_por_claves(lista, 'raza')
    for raza in listado_razas:
        print(f"Raza: {raza}")
        for personaje in lista:
            for personaje_raza in personaje['raza']:
                if personaje_raza == raza:
                    print(f"-> {personaje['nombre']} - Poder de Atque: {personaje['poder_ataque']}")
##4##
def buscar_personajes_por_habilidad(lista:list)->None:
    '''
    Brief: Agrupa a los personajes segun sus habilidades, ademas muestra los nombres sumado a la raza y el promedio de atque y defensa.
    Parameters:
        lista: str -> La lista donde va a buscar a los personajes para luego agruparlos
    Return: None
    '''
    habilidad_usario = input("Ingrese una habildiad: ")
    print(f"{habilidad_usario}:")
    for personaje in lista:
        split_race(personaje)
        for habilidad in personaje['hablidad']:
            if habilidad_usario == habilidad:
                promedio = (personaje['poder_ataque'] + personaje['poder_pela']) / 2
                print(f"Nombre: {personaje['nombre']} - Raza: {personaje['raza']} - Promedio: {promedio}")
