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
    c = False
    while c == False:
        c = pasajero.setTipo_hab(input("Ingrese Tipo Habitacion (Simple/Doble):"))
    pasajero.nombre = input("Ingrese Nombre:")
    pasajero.apellido = input("Ingrese Apellido:")
    c = False
    while c == False:
        try:
            pasajero.num_habitacion = int(input("Ingrese Num. Habitacion"))
            c = True
        except BaseException as error:
            print(f"Error:{error}")
    c = False
    while c == False:
        try:
            pasajero.cant_dias = int(input("Ingrese Cantidad de Dias:"))
            if pasajero.cant_dias > 0:
                c = True
        except BaseException as error:
            print(f"Error:{error}")
    return np.append(arreglo_huesped, pasajero)

def buscarHuesped(arreglo_huesped):
    rut = input("Ingrese Rut:")
    flag = False
    for huesped in arreglo_huesped:
        if rut == huesped.rut:
            flag = True
            print("Datos del Huesped")
            print(f"Rut   : {huesped.rut}")
            print(f"Nombre: {huesped.nombre} {huesped.apellido}")
            print(f"Numero Habitacion : {huesped.num_habitacion}")
            print(f"Tipo Habitacion   : {huesped.tipo_hab}")
            print(f"Cantidad de Dias  : {huesped.cant_dias}")
            print(f"Precio Habitacion :${huesped.precio}")
            total = huesped.cant_dias * huesped.precio
            print(f"Total Estadia     :${total}")
            break
    if flag == False:
        print("Rut de huesped no existe")

def listaCompleta(arreglo_huesped):
    folio = rn.randint(1000,8000)
    print(f"Numero Folio: {folio}")
    print("Lista Completa de Huespedes")
    total = 0
    for huesped in arreglo_huesped:
        print(f"{huesped.codigo_pasajero} {huesped.nombre} {huesped.apellido} {huesped.tipo_hab} {huesped.cant_dias}")
        total += huesped.cant_dias * huesped.precio
    print(f"Total General: ${total}")

def listados(arreglo_huesped):
    print("1) Listado Completo")
    print("2) Lista Huesped Particular")
    print("3) Salir")
    try:
        op_lista = int(input("Seleccione (1-3):"))
        match op_lista:
            case 1:
                listaCompleta(arreglo_huesped)
            case 2:
                buscarHuesped(arreglo_huesped)
    except BaseException as error:
        print(f"Error:{error}")

def salir():
    print("Autor: Juanito Simio v.1, adiossss ")
    return False

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
            case 2:
                buscarHuesped(arreglo_huesped)
            case 3:
                listados(arreglo_huesped)
            case 4:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")