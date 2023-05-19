from data_import import *
from def_dos_a_cuatro import *
from batalla import *
from def_6 import *

def imprimir_menu():
    '''
    Brief: Imprime las opciones del menu
    Parameters:
        None
    Return: None
    '''
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
    '''
    Brief: Indica si el un input es un numero o no.
    Parameters:
        string_numero: str -> El numero que va a analizar
    Return: boolean (si es un numero el valor sera True y si es una letra el valor sera False)
    '''
    return string_numero.isnumeric()

def numero_usario()->int:
    '''
    Brief: Le pide al usario que ingrese un numero, luego la analiza con la funcion anteriro y si no lo es le vuelve a pedir que ingrese un numero.
    Parameters:
        None
    Return: int
    '''
    imprimir_menu()
    respuesta = input("Ingrese una opcion: ")
    validacion = validar_entero(respuesta)
    if validacion == True:
        return int(respuesta)

def mostrar_menu(lista)->None:
    '''
    Brief: Realiza el match para ejecutar las funciones linkeadas a cada numero.
    Parameters:
        lista: list -> lista que le vamos a pasar a la llamada de las funciones
    Return: None
    '''
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

mostrar_menu(lista_principal)