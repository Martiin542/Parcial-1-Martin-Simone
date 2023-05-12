from importe_archivos  import *

import string
import json

def generar_nombre_archivo(raza, habilidad):
    nombre_archivo = f"{raza}_{habilidad}.json"
    nombre_archivo = "_" + nombre_archivo
    return nombre_archivo


def guardar_archivo_json(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def guardar_datos(lista):
    raza_usuario = validacion_ingresos(lista, 'race', "una raza: ")
    habilidad_usuario = validacion_ingresos(lista, 'ability', "una habilidad: ")
    data_personajes = {
        "personajes": []
    }

    personajes_encontrados = False

    for personaje in lista:
        if raza_usuario.lower() in personaje["race"].lower() and habilidad_usuario.lower() in personaje["ability"].lower():
            data_personajes["personajes"].append({
                "name": personaje["name"],
                "attack_power": personaje["attack_power"],
                "ability": personaje["ability"]
            })
            personajes_encontrados = True

    if personajes_encontrados:
        nombre_archivo = generar_nombre_archivo(raza_usuario, habilidad_usuario)
        guardar_archivo_json(nombre_archivo, data_personajes)
        return nombre_archivo
    else:
        print("No hay personajes que cumplan con los requisitos.")
        return None

guardar_datos(lista_principal)