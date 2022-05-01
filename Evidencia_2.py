from collections import namedtuple
import csv
import datetime

class Servicios:
    # Declaro las propiedades
    Folio=0
    Fecha=datetime
    Monto=0
    Servicio=""
    Acumulado=float
    # Genero el método constructor
    def _init_(self, folio, fecha, monto, servicio, acumulado) -> None:
        self.Folio=folio
        self.Fecha=fecha
        self.Monto=monto
        self.Servicio=servicio
        self.Acumulado=acumulado
    def MostrarInfo(self):
        print("{} -> {} {} {}".format(self.Folio,self.Fecha,self.Monto,self.Servicio,self.Acumulado))

Serv=[]

with open("Servicios.csv") as archivo_csv:
    
    lector = csv.reader(archivo_csv, delimiter=",")
    numero_linea=0
    
    for registro in lector:
        numero_linea=numero_linea+1
        if (not numero_linea==1):
            temporal=Servicios(registro[0],registro[1],registro[2],registro[3])
            Serv.append(temporal)
            
def Registrar_servicio():
    global Serv
    while True:
        folio=input("\nDame el folio a buscar:")
        if (folio==""):
            # Si se omite el folio, se sale a menú
            break
        else:
            # Si el parograma llega a esta línea, quiere decir que el folio no se omitió, 
            # entonces revisa si ya existe el registro.
            indice=BuscarFolio(folio)
            if (indice!=-1):
                print("\nEse folio ya existe. Intente otra.")
                continue
            else:
                fecha=input("Dame una fecha DD/MM/AAAA: ")
                servicio=input("Tipo de servicio: ")
                monto=input("Monto a pagar: ")
                _acumulado = (0.16)
                acumulado = (monto * _acumulado)
                temporal=Servicios(folio, fecha, monto, servicio, acumulado)
                # La agrego a la colección.
                Serv.append(temporal)
                break

def BuscarFolio(_folio):
    global Serv
    contador=-1
    indice=-1
    # Busca si existe un elemento con ese folio
    for var in Serv:
        contador=contador+1
        if (var.Folio==_folio):
            indice=contador
            break
    return indice

def BuscarFecha(_fecha):
    global Serv
    contador=-1
    indice=-1
    # Busca si existe un elemento con esa fecha
    for var in Serv:
        contador=contador+1
        if (var.Fecha==_fecha):
            indice=contador
            break
    return indice

def BuscarServicio():
    global Serv
    folio=input("\nDame el folio a buscar: ")
    if (not folio==""):
        indice=BuscarFolio(folio)
        if (indice==-1):
            print("\nNo se encontraron coincidencias")
        else:
            print(" ")
            Serv[indice].MostrarInfo()


def BuscarServicioFecha():
    global Serv
    fecha=input("\nDame la fecha a buscar: ")
    if (not fecha==""):
        indice=BuscarFolio(fecha)
        if (indice==-1):
            print("\nNo se encontraron coincidencias")
        else:
            print(" ")
            Serv[indice].MostrarInfo()


while True:
    print(" ")
    print("-"*50)
    print("MENÚ PRINCIPAL - Reparacion de computadoras y aparatos diversos")
    print("-"*50)
    print("[r] Registrar un servicio")
    print("[c] Consultar un servicio")
    print("[s] Consultar servicio en fecha especificada")
    print("[x] Salir")
    opcion=input("Qué opción deseas: ")
    if (opcion=="x"):
        break
    if (opcion=="r"):
        Registrar_servicio()
    if (opcion=="c"):
        BuscarServicio()
    if (opcion=="s"):
        BuscarServicioFecha()
