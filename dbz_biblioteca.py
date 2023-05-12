import re
import datetime
import random

def parser_csv(ruta:str):
    with open(ruta, 'r', encoding = "utf-8") as archivo:
        lista = []
        for linea in archivo:
            lectura = re.split(",", linea)
            personaje = {}
            personaje['ID'] = int(lectura[0])
            personaje['name'] = lectura[1] 
            personaje['race'] = re.split(r"-(?=[H])",lectura[2]) # Separa el string cuando hay un - seguido de una H (mayuscula)
            personaje['fight_power'] = int(lectura[3])
            personaje['attack_power'] = int(lectura[4])
            personaje['ability'] = [elemento.strip() for elemento in re.split(r'\|\$\%', lectura[5])] # Separa las habilidades por |$% , y una vez que los separa itera la lista con un for para hacerle un strip()(saca los espacios en blanco) a cada elemento
            lista.append(personaje)
    return lista

# 2
def contador_caracteristicas(lista:list, clave:str):
    contador_caracteristicas = {}
    for personaje in lista:
        caracteristicas = personaje[clave]
        for caracteristica in caracteristicas:
            if caracteristica in contador_caracteristicas:
                contador_caracteristicas[caracteristica] += 1
            else:
                contador_caracteristicas[caracteristica] = 1
    return contador_caracteristicas

def creador_de_listas(lista:list, clave:str):
    diccionario = {}
    for personaje in lista:
        for caracteristica in personaje[clave]:
            if caracteristica in diccionario:
                diccionario[caracteristica].append((personaje['ID'], personaje['name'], personaje['fight_power'], personaje['attack_power']))
            else:
                diccionario[caracteristica] = [(personaje['ID'], personaje['name'], personaje['fight_power'], personaje['attack_power'])]
    return diccionario

#3
def listar_personaje_por_raza(lista:list):
    diccionario_raza = creador_de_listas(lista, 'race')
    
    for clave, personajes in diccionario_raza.items():
        print(f"{clave}")
        for  heroe in personajes:
            print(f"Nombre: {heroe[1]}, Poder de ataque: {heroe[3]}")

#4
def buscar_personaje_por_habilidad(lista:list):
    habilidad_del_usario = input("Ingrese una habilidad: ")
    for personaje in lista:
        habilidades = personaje['ability']
        for heroe in habilidades:
            if heroe == habilidad_del_usario:
                print(heroe['name'])


lista_principal = parser_csv('DBZ.csv')

#contador_caracteristicas(lista_principal, 'race')
#print(listar_personaje_por_valor(lista_principal, 'race'))
#print(creador_de_listas(lista_principal, 'ability'))
#listar_personaje_por_raza(lista_principal)
#mostrar_heroes_por_habilidad(lista_principal, 'Summon Majins')
buscar_personaje_por_habilidad(lista_principal)



#print(lista_principal)


# def jugarBatalla(lista:list):
#     fecha_Actual = datetime.datetime.now()
#     pick_usuario = input("Elige el personaje con el que desee pelear: ")
#     num_random = random.randint(0,35)
#     poder_maquina = 0
#     nombre_makina = ''
    
#     for personaje in lista:
#         if pick_usuario == personaje["name"]:
#             poder_usario = personaje["attack_power"]
#         elif num_random == personaje["ID"]:
#             poder_maquina = personaje["attack_power"]
#             nombre_makina = personaje["name"]

#     print(poder_usario)
#     print(poder_maquina)
#     if poder_usario > poder_maquina:
#         print(f"El ganador es {pick_usuario} y el perdedor es {nombre_makina}")



# def listar_personaje_por_raza(lista:list):
#     diccionario_raza = {}
#     for personaje in lista:
#         for raza in personaje['race']:
#             if raza in diccionario_raza:
#                 diccionario_raza[raza].append((personaje['name'], personaje['attack_power']))
#             else:
#                 diccionario_raza[raza] = [(personaje['name'], personaje['attack_power'])]
#     for categoria, personajes in diccionario_raza.items():
#         print(f"{categoria}")
#         for pesonaje, poder in personajes:
#             print(f"Nombre: {pesonaje}, Poder de ataque: {poder}")
#         print()

# #4
# def personaje_por_habilidad(lista:list):
#     habilidad_usuario = input("Ingresar una habilidad: ")
#     diccionario_habilidad = {}
#     for personaje in lista:
#         for habildiad in personaje['ability']:
#             if habildiad in diccionario_habilidad:
#                 diccionario_habilidad[habildiad].append((personaje['name'], personaje['attack_power']))
#             else:
#                 diccionario_habilidad[habildiad] = [(personaje['name'], personaje['attack_power'])]
#     return diccionario_habilidad