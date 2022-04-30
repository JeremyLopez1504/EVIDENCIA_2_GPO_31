from collections import namedtuple
import csv
import datetime

class Servicios:
    # Declaro las propiedades
    Folio=0
    Fecha=datetime
    Monto=0
    Servicio=" "
    Acumulado=0
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
        folio=input("\nDame la matrícula a buscar:")
        if folio.keys():
            nueva_clave= max(folio.keys())+1
        else:
            nueva_clave=1
            folio[nueva_clave]=Serv
        if (folio==""):
            # Si se omite la matrícula, se sale a menú
            break
        else:
            # Si el parograma llega a esta línea, quiere decir que matrícula no se omitió, 
            # entonces revisa si ya existe el registro.
            indice=BuscarFolio(folio)
            if (indice!=-1):
                # Si indice no es -1 quiere decir que la matrícula ya existe, y manda
                # el mensaje de que el alta ya no se puede ejecutar.
                print("\nEsa matrícula ya existe. Intente otra.")
                continue
            else:
                # Si el programa llega a esta línea, quiere decir que matrícula no existe,
                # y se puede dar de alta.
                # Se preguntan los datos faltantes.
                fecha=input("Dame una fecha DD/MM/AAAA: ")
                servicio=input("Tipo de servicio: ")
                monto=input("Monto a pagar: ")
                acumulado=input((monto)*0.16)
                # Crear una instancia de Alumno, con los datos
                temporal=Servicios(fecha, servicio, monto, acumulado)
                # La agrego a la colección.
                Serv.append(temporal)
                break

def BuscarFolio(_folio):
    global Serv
    contador=-1
    indice=-1
    # Busca si existe un elemento con esa matrícula
    for var in Serv:
        contador=contador+1
        if (var.Matricula==_folio):
            indice=contador
            break
    return indice

def BuscarServicio():
    global Serv
    # Pregunta una matrícula. Si existe el alumno, lo muestra usando el
    # método mostrar info, o de lo contrario, reporta "No encontrado".
    # Si se omite el dato, no hace nada.
    folio=input("\nDame la matrícula a buscar: ")
    if (not folio==""):
        indice=BuscarFolio(folio)
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
        ()