class Huesped:
    codigo_pasajero=''
    rut=''
    nombre=''
    apellido=''
    num_habitacion=0
    precio=0
    cant_dias=0
    tipo_hab=''

    def __init__(self):
        self.codigo_pasajero='001'
        self.rut='12345678-0'
        self.nombre='S/N'
        self.apellido='S/A'
        self.num_habitacion=1
        self.precio=35000
        self.cant_dias=1
        self.tipo_hab='Simple'

    def setCodigo_pasajero(self, codigo):
        if len(codigo) >= 2 and len(codigo) <= 15:
            self.codigo_pasajero = codigo
            return True
        else:
            print("codigo incorrecto, debe estar entre 2 y 15 caracteres")
            return False

    def setRut(self,rut):
        if len(rut) == 10:
            if rut[0:8].isdigit() and rut[8:9] == '-' and (rut[9:10].isdigit() or rut[9:10].upper() == 'K'):
                self.rut = rut
                return True
            else:
                print('no posee formato correcto Ej. 01254125-9')
                return False
        else:
            print('largo incorrecto, debe tener un largo de 10')
            return False


    def setPrecio(self,precio):
        if precio >= 35000 and precio <= 56000:
            self.precio = precio
            return True
        else:
            print("el precio debe estar entre 35000 y 56000")
            return  False

    def setTipo_hab(self,tipo):
        if tipo.upper() == 'SIMPLE' or tipo.upper() == 'DOBLE':
            self.tipo_hab = tipo
            return True
        else:
            print("tipo de habitacion simple o doble")
            return False