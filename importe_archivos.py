import re
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

lista_principal = parser_csv('DBZ.csv')
lista_ajustada_raza = ajustar_diccionarios(lista_principal, 'race')
lista_ajustada_habilidad = ajustar_diccionarios(lista_principal, 'ability')

print