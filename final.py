import re
import datetime
import random
import json

def parser_csv(ruta:str)->list:
    '''
    Brief: 
    Parameters: Recibe la ruta de un archivo CSV y lee su contenido para convertirlo en una lista de diccionarios. Cada diccionario representa un personaje y sus caracteristicas, luego devuelve la lista de personajes.
        ruta: str ->  La ruta del archivo CSV sobre la va a analizar y convertir en una lista de personajes.
    Return: Una lista de diccionarios, donde cada diccionario representa un personaje con sus atributos.
    '''
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

def ajustar_diccionarios(lista_personajes, clave:str):
    '''
    Brief: 
    Parameters: Recibe la ruta de un archivo CSV y lee su contenido para convertirlo en una lista de diccionarios. Cada diccionario representa un personaje y sus caracteristicas, luego devuelve la lista de personajes.
        ruta: str ->  La ruta del archivo CSV sobre la va a analizar y convertir en una lista de personajes.
    Return: Una lista de diccionarios, donde cada diccionario representa un personaje con sus atributos.
    '''
    nuevos_personajes = []
    for personaje in lista_personajes:
        razas = personaje[clave]
        if len(razas) > 1:
            for i in range(1, len(razas)):
                nuevo_personaje = dict(personaje)  # Copiar el diccionario existente
                nuevo_personaje[clave] = razas[i]  # Reemplazar la raza por la segunda raza
                nuevos_personajes.append(nuevo_personaje)
        personaje[clave] = razas[0]  # Mantener solo la primera raza
        nuevos_personajes.append(personaje)
    return nuevos_personajes

# 2
def contar_caracteristica(lista:list, clave:str)->dict:
    diccionario_caracteristicas = {}
    for personaje in lista:
        if personaje[clave] in diccionario_caracteristicas:
            diccionario_caracteristicas[personaje[clave]] += 1
        else:
            diccionario_caracteristicas[personaje[clave]] = 1 
    return diccionario_caracteristicas
# 3
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
# 4
def buscar_personajes_por_habilidad(lista:list):
    habilidad_usario = input("Ingrese una habildiad: ")
    print(f"{habilidad_usario}:")
    for personaje in lista:
        promedio = (personaje['attack_power'] + personaje['fight_power']) / 2
        if habilidad_usario == personaje['ability']:
            print(f"Nombre: {personaje['name']} - Raza: {personaje['race']} - Promedio: {promedio}")

##############input############

# 5
def selecion_de_personaje_usario(lista:list):
    personaje_usario = input('Elije un personaje para la batalla!: ')
    for personaje in lista:
        if personaje_usario == personaje['name']:
            poder_del_usuario = personaje['attack_power']
    return personaje_usario, poder_del_usuario

def selecion_de_personaje_maquina(lista:list):
    numero_random = random.randint(0, len(lista))
    for personaje in lista:
        if numero_random == personaje['ID']:
            poder_maquina = personaje["attack_power"]
            nombre_maquina = personaje["name"]
    return nombre_maquina, poder_maquina

def jugar_batalla(lista:list):
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
    fecha_actual = datetime.datetime.now()
    ganador, perdedor = jugar_batalla(lista)
    with open("resultado.txt", "a", encoding = "utf-8") as archivo:
        archivo.write(f"Personaje ganador: {ganador} | Personaje perdedor: {perdedor} | {fecha_actual}\n")

#6
def encontrar_personajes(lista:list):
    raza_usuario = input('Ingrese una raza: ')
    habilidad_usuario = input('Ingrese una habilidad: ')
    personajes_lista = []
    for personaje in lista:
        if raza_usuario in personaje['race'] and habilidad_usuario in personaje['ability']:
            personaje_diccionario = {}
            personaje_diccionario['name'] = personaje['name']
            personaje_diccionario['attack_power'] = personaje['attack_power']
            personaje_diccionario['ability'] = personaje['ability']
            personajes_lista.append(personaje_diccionario)
    return personajes_lista


lista_principal = parser_csv('DBZ.csv')
#print(lista_principal)
lista_ajustada_raza = ajustar_diccionarios(lista_principal, 'race')
lista_ajustada_habilidad = ajustar_diccionarios(lista_principal, 'ability')


#print(contar_caracteristica(lista_ajustada_raza, 'race'))
#listar_agrupados(lista_principal, 'race')
#buscar_personajes_por_habilidad(lista_ajustada_habilidad)
#print(jugar_batalla(lista_principal))
#guardar_txt(lista_principal)
#print(seleccion_raza_habiliad(lista_principal))
main(lista_principal)
