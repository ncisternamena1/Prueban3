
from clases import *
import random as rn
import numpy as np

arreglo_libro = np.array([])
ciclo = True

def ingresarlibro(arreglo_libro):
    persona = libro()
    c =False
    while c == False:
        c = persona.setCodigo_libro(input("Ingrese el codigo del libro:"))
    c = False
    while c == False:
        try:
            c = persona.setPrecio(int(input("Ingrese precio:")))
        except BaseException as error:
            print(f"Error: {error}")
    c = False


def salir():
    print("Gracias por preferirnos")
    return False


while ciclo:
    print("Menu")
    print("1) Grabar libro")
    print("2) Buscar libro")
    print("3) imprimir informes")
    print("4) Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                print("Ingresar libro")
                arreglo_huesped = ingresarlibro(arreglo_libro)
            case 2:
                print("Buscar libro")
            case 3:
                print("Listados")
            case 4:
                print("Saliendo")
                ciclo = salir() #quebrar el while, esto vale un punto
            case _:
                print("Opcion incorrecta")
    except BaseException as error:
        print(f"Error: {error}")




