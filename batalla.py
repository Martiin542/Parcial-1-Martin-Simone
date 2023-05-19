from data_import import *
import datetime
import random

def selecion_de_personaje_usario(lista:list)->str:
    '''
    Brief: Solicita al usuario que elija un personaje para la batalla y luego busca en la lista el personaje seleccionado.
    Parameters:
        lista: str -> La lista donde va a comparar el nombre del personaje de cada diccionario con el del usario.
    Return: El personaje que elijio el usario y el poder de atque del personaje que elijio (str).
    '''
    personaje_usario = validar_input(lista, 'nombre')
    for personaje in lista:
        if personaje_usario == personaje['nombre']:
            poder_del_usuario = personaje['poder_ataque']
    return personaje_usario, poder_del_usuario

def selecion_de_personaje_maquina(lista:list)->str:
    '''
    Brief: Genera un número aleatorio y busca en la lista el personaje cuyo ID coincide con el número generado. 
    Parameters:
        lista: str ->  La lista donde va a comparar el numero random del personaje de cada id de los personajes. 
    Return: El personaje que elijio la maquina y el poder de atque del mismo
    '''
    numero_random = random.randint(0, len(lista))
    for personaje in lista:
        if numero_random == personaje['ID']:
            poder_maquina = personaje["poder_ataque"]
            nombre_maquina = personaje["nombre"]
    return nombre_maquina, poder_maquina

def jugar_batalla(lista:list)->str:
    '''
    Brief: Realiza la compracion del poder de la maquina contra el del usario y determina el ganador.
    Parameters:
        lista: str ->  La lista que le vamos a pasar a las funciones encargadas de buscar los nombres y el poder de atque.
    Return: El nombre del ganador y el perdedor 
    '''
    personaje_del_usario, poder_usario = selecion_de_personaje_usario(lista)
    personaje_maquina, poder_maquina = selecion_de_personaje_maquina(lista)
    if poder_usario > poder_maquina:
        ganador = personaje_del_usario
        perdedor = personaje_maquina
    elif poder_usario == poder_maquina:
        ganador = f"Empate"
        perdedor = f"No hay."
    else:
        ganador = personaje_maquina
        perdedor = personaje_del_usario
    return ganador, perdedor

def guardar_txt(lista:list)->None:
    '''
    Brief: Guarda el nombre del ganador y perdedor en un archivo txt, y le agrega la hora en la que se realizo la batalla
    Parameters:
        lista: str ->  La lista que le pasamos a la funcion batalla
    Return: None, genera el txt
    '''
    fecha_actual = datetime.datetime.now()
    ganador, perdedor = jugar_batalla(lista)
    print(f"Personaje ganador: {ganador} | Personaje perdedor: {perdedor}")
    with open("resultado.txt", "a", encoding = "utf-8") as archivo:
        archivo.write(f"Personaje ganador: {ganador} | Personaje perdedor: {perdedor} | {fecha_actual}\n")


