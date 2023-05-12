import re
import datetime
import random
import json

def parser_csv(ruta:str)->list:
    '''
    Brief: 
    Parameters: Recibe la ruta de un archivo CSV y lee su contenido para convertirlo en una lista de diccionarios. Cada diccionario representa un personaje y sus caracteristicas, luego devuelve la lista de personajes.
        ruta: str ->  La ruta del archivo CSV sobre la va a analizar y convertir en una lista de personajes
    Return: Una lista de diccionarios, donde cada diccionario representa un personaje con sus atributos
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

def ajustar_diccionarios(lista:list, clave:str)->list:
    '''
    Brief: Recibe una lista de diccionarios donde estan los personajes y una clave específica. Si alguna clave tiene más de un valor, se crean nuevos diccionarios para cada valor adicional y se reemplaza el valor original por el siguiente valor de la lista. Finalmente, devuelve una nueva lista de diccionarios actualizados
    Parameters:
        lista: str -> La lista de diccionarios que representan personajes, donde cada diccionario contiene características del personaje
        clave:str -> La clave donde en las cuales si encunetra listas separa los valores en diccionarios clonados
    Return: Una nueva lista de diccionarios, donde estan los diccionarios originales y los nuevos
    '''
    nuevos_personajes = []
    for personaje in lista:
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
    '''
    Brief: Recibe una lista de diccionarios que representan personajes y una clave específica. cuenta cuántas veces aparece cada valor de la característica en la lista y devolver un diccionario que muestre esos conteos.
    Parameters:
        lista: str ->  Una lista de diccionarios con la informacion de los personajes
        clave:str -> La característica específica que quieres contar en los personajes
    Return: Un diccionario que muestra el recuento de cada valor de la característica
    '''
    diccionario_caracteristicas = {}
    for personaje in lista:
        if personaje[clave] in diccionario_caracteristicas:
            diccionario_caracteristicas[personaje[clave]] += 1
        else:
            diccionario_caracteristicas[personaje[clave]] = 1 
    return diccionario_caracteristicas
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

###Input
def validacion_ingresos(lista: list, clave: str, pregunta:str) -> str:
    '''
    Brief: Recibe una lista de diccionarios que representan personajes, una clave específica y una pregunta para solicitar un valor al usuario. alida si el valor ingresado por el usuario coincide con algún valor de la clave en los personajes de la lista
    Parameters:
        lista: str -> Lista de diccionarios que representan personajes, donde cada diccionario contiene características del personaje
        clave:str ->  La clave específica utilizada para realizar la validación
        pregunta:str ->  La pregunta que se muestra al usuario al solicitar el valor
    Return: Un string con lo que ingreso el usario
    '''
    valor = input(f"Ingrese {pregunta}: ")
    for personaje in lista:
        if valor == personaje.get(clave):
            return valor
    return None

# 4
def buscar_personajes_por_habilidad(lista:list):
    '''
    Brief: Agrupa a los personajes segun sus habilidades, ademas muestra los nombres, la raza y el promedio de atque y defensa
    Parameters:
        lista: str -> La lista donde va a buscar a los personajes para luego agruparlos
    Return: None
    '''
    habilidad_usario = input('Ingrese una habilidad: ')
    print(f"{habilidad_usario}:")
    for personaje in lista:
        promedio = (personaje['attack_power'] + personaje['fight_power']) / 2
        if habilidad_usario == personaje['ability']:
            print(f"Nombre: {personaje['name']} - Raza: {personaje['race']} - Promedio: {promedio}")

# 5
def selecion_de_personaje_usario(lista:list)->str:
    '''
    Brief: Solicita al usuario que elija un personaje para la batalla y luego busca en la lista el personaje seleccionado. Devuelve el nombre del personaje elegido por el usuario y su poder de ataque
    Parameters:
        lista: str -> La lista donde va a comparar el nombre del personaje de cada diccionario con el del usario
    Return: El personaje que elijio el usario y el poder de atque del personaje que elijio
    '''
    personaje_usario = input('Elije un personaje para la batalla!: ')
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

#6
def guardar_jason(lista:list):
    raza_usario = validacion_ingresos(lista, 'race', "una raza: ")
    habilidad_usario = validacion_ingresos(lista, 'ability', "una habilidad: ")
    data_personajes = {}
    data_personajes["personajes"] = []
    
    personaje_encontrado = False
    
    for personaje in lista:
        if raza_usario in personaje["race"] and habilidad_usario in personaje["ability"]:
            data_personajes["personajes"].append({"nombre": personaje["name"],
                                                "poder de ataque": personaje["attack_power"],
                                                "habilidades": personaje["ability"]})
            personaje_encontrado = True
    
    if personaje_encontrado:
        nombre_archivo = f"{raza_usario}_{habilidad_usario}.json"
        nombre_con_guiones = nombre_archivo.replace(" ","_")
        with open(nombre_con_guiones, "w") as mi_archivo:
            json.dump(data_personajes, mi_archivo, indent=4)
        return nombre_con_guiones
    else:
        print("No hay personajes que cumplan con los requisitos")
        return None

#7
# def leer_json():
#     with open("agenda.json", "r") as mi_archivo:
#         data = json.load(mi_archivo)
#     print(data)



lista_principal = parser_csv('DBZ.csv')
#print(lista_principal)
lista_ajustada_raza = ajustar_diccionarios(lista_principal, 'race')
lista_ajustada_habilidad = ajustar_diccionarios(lista_principal, 'ability')

guardar_jason(lista_principal, 'Saiyan', 'Gigantic Meteor')
# print(contar_caracteristica(lista_ajustada_raza, 'race'))
# listar_agrupados(lista_principal, 'race')
# buscar_personajes_por_habilidad(lista_ajustada_habilidad)
# print(jugar_batalla(lista_principal))
# guardar_txt(lista_principal)
# print(seleccion_raza_habiliad(lista_principal))
# habilidades_usarios(lista_principal)

