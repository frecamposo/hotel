from Huesped import *
import random as rn
import numpy as np
############################################################
def ingresarHuesped(arreglo_huesped):
    pasajero = Huesped()

    c = False
    while c == False:
        c = pasajero.setCodigo_pasajero(input("Ingrese Codigo Pasajero:"))
    c = False
    while c == False:
        c = pasajero.setRut(input("Ingrese Rut Ej.12345678-9:"))
    c = False
    while c == False:
        try:
            c = pasajero.setPrecio(int(input("Ingrese Precio:")))
        except BaseException as error:
            print(f"Error:{error}")

############################################################
arreglo_huesped = np.array([])
ciclo = True
while ciclo:
    print("Menu Hotel Continental")
    print("1) Ingresar Huesped")
    print("2) Buscar Huesped")
    print("3) Listados")
    print("4) salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                arreglo_huesped = ingresarHuesped(arreglo_huesped)
    except BaseException as error:
        print(f"Error:{error}")