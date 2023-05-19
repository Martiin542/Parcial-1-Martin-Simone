import re
import json
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
            personaje['raza'] = lectura[2] # Separa el string cuando hay un - seguido de una H (mayuscula)
            personaje['poder_pela'] = int(lectura[3])
            personaje['poder_ataque'] = int(lectura[4])
            personaje['hablidad'] = lectura[5] # Separa las habilidades por |$% , y una vez que los separa itera la lista con un for para hacerle un strip()(saca los espacios en blanco) a cada elemento
            lista.append(personaje)
    return lista
##spliter##
def split_race(personaje:str)->None:
    '''
    Brief: Divide a las claves 'raza' y 'hablidad'
    Parameters: 
        ruta: str ->  La ruta del archivo CSV sobre la va a analizar y convertir en una lista de personajes
    Return: Una lista de diccionarios, donde cada diccionario representa un personaje con sus atributos
    '''
    personaje['raza'] = re.split(r"-(?=[H])", personaje['raza'])
    personaje['hablidad'] = [elemento.strip() for elemento in re.split(r'\|\$\%', personaje['hablidad'])]
##listas por clave##
def listar_por_claves(lista:list, clave:str)->list:
    lista_de_claves = []
    for personaje in lista:
        split_race(personaje)
        for caracteristica in personaje[clave]:
            if caracteristica not in lista_de_claves:
                lista_de_claves.append(caracteristica)
    return lista_de_claves
##input##
def validar_input(lista:list, campo:str):
    while True:
        valor = input(f"Ingrese el valor de {campo}: ")
        for elemento in lista:
            if elemento['nombre'] == valor or elemento['raza'] == valor or elemento['hablidad'] == valor:
                return elemento[campo]
        print("Los valores ingrsados no son validos.")

def contar_por_raza(lista:list)->dict:
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
def listar_personajes_por_raza(lista:list):
    listado_razas = listar_por_claves(lista, 'raza')
    for raza in listado_razas:
        print(f"Raza: {raza}")
        for personaje in lista:
            for personaje_raza in personaje['raza']:
                if personaje_raza == raza:
                    print(f"-> {personaje['nombre']} - Poder de Atque: {personaje['poder_ataque']}")
##4##
def buscar_personajes_por_habilidad(lista:list):
    habilidad_usario = validar_input(lista, 'hablidad')
    print(f"{habilidad_usario}:")
    for personaje in lista:
        split_race(personaje)
        for habilidad in personaje['hablidad']:
            if habilidad_usario == habilidad:
                promedio = (personaje['poder_ataque'] + personaje['poder_pela']) / 2
                print(f"Nombre: {personaje['nombre']} - Raza: {personaje['raza']} - Promedio: {promedio}")

def listar_personajes_por_raza_habilidad(lista:list):
    habilidad_usario = validar_input(lista, 'hablidad')
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

def guardar_personajes_en_json(lista:list):
    personajes_filtrados, nombre_archivo = listar_personajes_por_raza_habilidad(lista)
    with open(nombre_archivo, 'w') as mi_archivo:
        json.dump(personajes_filtrados, mi_archivo, indent = 4)

def leer_json():
    archivo = input('ingrese un archivo: ')
    with open(archivo, "r") as mi_archivo:
        data = json.load(mi_archivo)
    print(data)

import datetime
import random

def selecion_de_personaje_usario(lista:list)->str:
    personaje_usario = validar_input(lista, 'nombre')
    for personaje in lista:
        if personaje_usario == personaje['nombre']:
            poder_del_usuario = personaje['poder_ataque']
    return personaje_usario, poder_del_usuario

def selecion_de_personaje_maquina(lista:list)->str:
    numero_random = random.randint(0, len(lista))
    for personaje in lista:
        if numero_random == personaje['ID']:
            poder_maquina = personaje["poder_ataque"]
            nombre_maquina = personaje["nombre"]
    return nombre_maquina, poder_maquina

def jugar_batalla(lista:list)->str:
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

def guardar_txt(lista:list):
    fecha_actual = datetime.datetime.now()
    ganador, perdedor = jugar_batalla(lista)
    print(f"Personaje ganador: {ganador} | Personaje perdedor: {perdedor}")
    with open("resultado.txt", "a", encoding = "utf-8") as archivo:
        archivo.write(f"Personaje ganador: {ganador} | Personaje perdedor: {perdedor} | {fecha_actual}\n")

def imprimir_menu():
    print(
    '''
    1. Mostrar cantidad de personajes por raza
    2. Listar personaje por raza
    3. Mostrar los personajes con la misma habilidad
    4. Batalla
    5. Generar listado con los personajes con la misma raza y habildiad (json)
    6. lerr json
    7. salir
    ''')

def validar_entero(string_numero:str)->bool:
    return string_numero.isnumeric()

def numero_usario():
    imprimir_menu()
    respuesta = input("Ingrese una opcion: ")
    validacion = validar_entero(respuesta)
    if validacion == True:
        return int(respuesta)


def mostrar_menu(lista):
    seguir = True
    while seguir == True:
        respuesta = numero_usario()
        match respuesta:
            case 1: 
                contar_por_raza(lista)
            case 2:
                listar_personajes_por_raza(lista)
            case 3:
                buscar_personajes_por_habilidad(lista)
            case 4:
                guardar_txt(lista)
            case 5:
                guardar_personajes_en_json(lista)
            case 6:
                leer_json()
            case 7:
                seguir = False



lista_principal = parser_csv('DBZ.csv')
mostrar_menu(lista_principal)