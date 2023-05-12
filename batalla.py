from importe_archivos import *
import datetime
import random
def selecion_de_personaje_usario(lista:list)->str:
    '''
    Brief: Solicita al usuario que elija un personaje para la batalla y luego busca en la lista el personaje seleccionado. Devuelve el nombre del personaje elegido por el usuario y su poder de ataque
    Parameters:
        lista: str -> La lista donde va a comparar el nombre del personaje de cada diccionario con el del usario
    Return: El personaje que elijio el usario y el poder de atque del personaje que elijio
    '''
    personaje_usario = validacion_ingresos(lista, 'name', 'un heroe para la batalla!: ')
    for personaje in lista:
        if personaje_usario == personaje['name']:
            poder_del_usuario = personaje['attack_power']
    return personaje_usario, poder_del_usuario

def selecion_de_personaje_maquina(lista:list)->str:
    '''
    Brief: Genera un número aleatorio y busca en la lista el personaje cuyo ID coincide con el número generado. Devuelve el nombre del personaje seleccionado por la máquina y su poder de ataque.
    Parameters:
        lista: str ->  La lista donde va a comparar el numero random del personaje de cada id de los personajes. 
    Return: El personaje que elijio la maquina y el poder de atque del mismo
    '''
    numero_random = random.randint(0, len(lista))
    for personaje in lista:
        if numero_random == personaje['ID']:
            poder_maquina = personaje["attack_power"]
            nombre_maquina = personaje["name"]
    return nombre_maquina, poder_maquina

def jugar_batalla(lista:list):
    '''
    Brief: Genera un número aleatorio y busca en la lista el personaje cuyo ID coincide con el número generado. Devuelve el nombre del personaje seleccionado por la máquina y su poder de ataque.
    Parameters:
        lista: str ->  La lista donde va a comparar el numero random del personaje de cada id de los personajes. 
    Return: El personaje que elijio la maquina y el poder de atque del mismo
    '''
    personaje_del_usario, poder_usario = selecion_de_personaje_usario(lista)
    personaje_maquina, poder_maquina = selecion_de_personaje_maquina(lista)
    if poder_usario > poder_maquina:
        ganador = personaje_del_usario
        perdedor = personaje_maquina
    else:
        ganador = personaje_maquina
        perdedor = personaje_del_usario
    return ganador, perdedor

def guardar_txt(lista:list):
    '''
    Brief: Ejecuta una batalla entre dos personajes utilizando la función jugar_batalla. Luego, guarda el resultado de la batalla en un archivo de texto llamado "resultado.txt", junto con la fecha y hora actual.
    Parameters:
        lista: str ->  La lista que le pasamos a la funcion batalla
    Return: El personaje que elijio la maquina y el poder de atque del mismo
    '''
    fecha_actual = datetime.datetime.now()
    ganador, perdedor = jugar_batalla(lista)
    with open("resultado.txt", "a", encoding = "utf-8") as archivo:
        archivo.write(f"Personaje ganador: {ganador} | Personaje perdedor: {perdedor} | {fecha_actual}\n")