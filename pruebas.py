import re
import random
def parser_csv(ruta:str):
    with open(ruta, 'r', encoding="utf-8") as archivo:
        lista = []
        for linea in archivo:
            lectura = re.split(",", linea)
            razas = re.split(r'-(?=[H])',lectura[2])
            for raza in razas:
                personaje = {}
                personaje['ID'] = int(lectura[0])
                personaje['name'] = lectura[1]
                personaje['race'] = raza.strip()
                personaje['fight_power'] = int(lectura[3])
                personaje['attack_power'] = int(lectura[4])
                personaje['ability'] = [elemento.strip() for elemento in re.split(r'\|\$\%', lectura[5])]
                lista.append(personaje)    
    return lista

def contar_caracteristica(lista:list, clave:str)->dict:
    diccionario_caracteristicas = {}
    for personaje in lista:
        if personaje[clave] in diccionario_caracteristicas:
            diccionario_caracteristicas[personaje[clave]] += 1
        else:
            diccionario_caracteristicas[personaje[clave]] = 1 
    return diccionario_caracteristicas

def listar_agrupados(lista:list, clave:str)->None:
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

def listar_personaje_por_habilidad(lista:list, habilidad:str):
    for personaje in lista:
        if habilidad == personaje['ability']:
            print(f"{personaje['name']}")
    else:
        print("error")

# def pruebas():
#     for raza in razas:
#         print(f'{raza.upper()}:')
#         if re.search(r"Saiyan", raza):
#             personajes_saiyan = [p for p in personajes if re.search(r"Saiyan(-Humano)?", p['raza'])]
#             for personaje in personajes_saiyan:
#                 nombre = personaje['nombre']
#                 poder_ataque = personaje['poder_ataque']
#                 print(f'\t- {nombre} ({poder_ataque} de poder de ataque)')
#         elif re.search(r"Androide", raza):
#             personajes_androide = [p for p in personajes if re.search(r"Androide(-Humano)?", p['raza'])]
#             for personaje in personajes_androide:
#                 nombre = personaje['nombre']
#                 poder_ataque = personaje['poder_ataque']
#                 print(f'\t- {nombre} ({poder_ataque} de poder de ataque)')
#         else:
#             for personaje in personajes:
#                 if personaje['raza'] == raza:
#                     nombre = personaje['nombre']
#                     poder_ataque = personaje['poder_ataque']
#                     print(f'\t- {nombre} ({poder_ataque} de poder de ataque)')



lista_personajes = parser_csv('DBZ.csv')


print(lista_personajes[10])
#listar_personaje_por_habilidad(lista_personajes, 'Barrera de energía')












# def batalla_por_habilidad(lista:list, nombre:str):
#     pick_del_usario = input('Ingrese el nombre de un personaje: ')
#     numero_random = random.randint(1, 35)
#     for personaje in lista:
#         if pick_del_usario == personaje['name']:
#             poder_del_usario = personaje['attack_power']
#         elif numero_random == personaje['ID']:
#             poder_de_la_maquina = personaje['attack_power']
    
#     if