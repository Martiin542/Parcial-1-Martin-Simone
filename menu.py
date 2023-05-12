from importe_archivos import *
from funciones_principales import *
from batalla import *
from parte_json import *
# lista_principal = parser_csv('DBZ.csv')
# lista_ajustada_raza = ajustar_diccionarios(lista_principal, 'race')
# lista_ajustada_habilidad = ajustar_diccionarios(lista_principal, 'ability')

def imprimir_dato(cadena:str)->None:
    '''
    Brief: Imprime en la consola lo que le pasemos por parametros
    Parameters: 
        cadena: str -> lo que queremos que imprima por consola
    Return: None
    '''
    print(cadena)

def imprimir_menu():
    imprimir_dato(
    '''
    1. Mostrar cantidad de personajes por raza
    2. Listar personaje por raza
    3. Mostrar personajes que poseen una misma habilidad
    4. Batalla
    5. json
    6. lerr json
    7. salir
    ''')

def numero_usario():
    imprimir_menu()
    respuesta = int(input("Ingrese una opcion: "))
    return respuesta


def mostrar_menu():
    seguir = True
    while seguir == True:
        respuesta = numero_usario()
        match respuesta:
            case 1: 
                contar_por_raza(lista_principal)
            case 2:
                listar_agrupados(lista_ajustada_raza, 'race')
            case 3:
                buscar_personajes_por_habilidad(lista_ajustada_habilidad)
            case 4:
                guardar_txt(lista_principal)
            case 5:
                guardar_datos(lista_principal)
            case 6:
                pass
            case 7:
                seguir = False

mostrar_menu()
#contar_por_raza()