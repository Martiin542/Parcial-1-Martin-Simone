from data_import import *
from def_dos_a_cuatro import *
import json
def listar_personajes_por_raza_habilidad(lista:list)->list:
    '''
    Brief: agrupa a los personajes que tengan la misma raza y la misma habilidad
    Parameters:
        lista: str -> La lista donde va a buscar a los personajes para luego agruparlos
    Return: list | string
    '''
    habilidad_usario = input("Ingrese una habilidad: ")
    raza_usario = validar_input(lista, 'raza')
    personajes_filtrados = []
    for personaje in lista:
        split_race(personaje)
        for habilidad in personaje['hablidad']:
            for raza in personaje['raza']:
                if habilidad_usario == habilidad and raza_usario == raza:
                    personajes_filtrados.append({
                        'nombre': personaje['nombre'],
                        'poder_de_ataque': personaje['poder_ataque'],
                        'habilidad': personaje['hablidad']
                    })
    nombre_archivo = f"{raza_usario}_{habilidad_usario}.json"
    return personajes_filtrados, nombre_archivo

def guardar_personajes_en_json(lista:list)->None:
    '''
    Brief: Guarda a la lista de personajes filtrados en un archivo json.
    Parameters:
        lista: str -> La lista que se le pasa a la funcion "listar_personajes_por_raza_habilidad"
    Return: None
    '''
    personajes_filtrados, nombre_archivo = listar_personajes_por_raza_habilidad(lista)
    with open(nombre_archivo, 'w') as mi_archivo:
        json.dump(personajes_filtrados, mi_archivo, indent = 4)

def leer_json():
    '''
    Brief: Lee los archivos creados por la funcion anteriro ("guardar_personajes_en_json")
    Parameters:
        None
    Return: None
    '''
    archivo = input('ingrese un archivo: ')
    with open(archivo, "r") as mi_archivo:
        data = json.load(mi_archivo)
    print(data)