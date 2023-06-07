#   ********---UNIDAD 3 POO - Ejercicio6 - VB---*********

import json
from pathlib import Path
import abc
from abc import ABC


class Vehiculo(ABC): 
    
    def __init__(self,modelo,cant,color,precio,marca):
        self.__modelo = modelo
        self.__cantPuertas = cant
        self.__color = color
        self.__precioBase = precio
        self.__marca = marca
        
    def getModelo(self):
        return self.__modelo
    def getCantPuertas(self):
        return self.__cantPuertas
    def getColor(self):
        return self.__color
    def getPrecioBase(self):
        return self.__precioBase
    def getMarca(self):
        return self.__marca
        
    @abc.abstractmethod
    def importVentas():
        pass

class Nuevo(Vehiculo):
    
    def __init__(self,modelo,cant,color,precio,marca,version):
        super().__init__(modelo,cant,color,precio,marca)
        self.__version = version
        
    def getDatos(self):
        print("- Modelo: {}\n- Cant de Puertas: {}".format(super().getModelo(), super().getCantPuertas()))
        print("- Color: {}\n- Precio: {}\n- Marca: {} ".format(super().getColor(),super().getPrecioBase(), super().getMarca()))  
        print("- Version: {}".format(self.__version))
  
    def importVentas(self):
        precioVenta = self.__precioBase + self.__precioBase * 0.1
        if self.__version == "full":
            precioVenta += self.__precioBase * 0.02
        return precio_venta
        
class Usado(Vehiculo):
    
    def __init__(self,modelo,cant,color,precio,marca,patente,año,km):
        super().__init__(modelo,cant,color,precio,marca)
        self.__patente = patente
        self.__año = año
        self.__kilometraje = km
        
    def getDatos(self):
        print("- Modelo: {}\n- Cant de Puertas: {}".format(super().getModelo(), super().getCantPuertas()))
        print("- Color: {}\n- Precio: {}\n- Marca: {} ".format(super().getColor(),super().getPrecioBase(), super().getMarca()))  
        print("- Patente: {}\n- Año: {}\n- Kilometraje: {}".format(self.__patente,self.__año,self.__kilometraje))
        
    def importVentas(self):
        antiguedad = date.today().year - self.__año
        porcentajeDescuento = antiguedad * 0.01
        if self.__kilometraje > 100000:
            porcentajeDescuento += 0.02
        precioVenta = self.precioBase - self.precio_base * porcentajeDescuento
        return precioVenta
            
        
class Nodo:
    
    __vehiculo: Vehiculo
    __sig: object
    
    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__sig = None
        
    def setSiguiente(self,siguiente):
        self.__sig = siguiente
    
    def getSiguiente(self):
        return self.__sig
    
    def getDato(self):
        return self.__vehiculo
    
    
class Lista:
    
    __comienzo: Nodo
    __actual: Nodo #
    __indice = 0#
    __tope = 0 #
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None #
    
    def __iter__(self): #
        return self
    
    def __next__(self): #
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        
    def agregarVehiculo(self,vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual=nodo #
        self.__tope +=1 #
        
    def mostrarVehiculos(self):
        aux = self.__comienzo
        while aux != None:
            aux.getDato().getDatos()
            aux = aux.getSiguiente()
            print("-----")
            
    def buscarVehiculo(self,posicion):
        pass
    
    def modificarPrecio(self,patente):
        pass
    
    def guardarDatosJson(self):
        pass
    
    
        
def cargarVehiculos(lista):
    i = 0
    with open("Activividades\\Ejercicio6\\vehiculos.json") as file:
        diccionario = json.load(file)
    for i in diccionario["vehiculos"]:
       if i["tipo"] == "nuevo":
           unVehiculo = Nuevo(i["modelo"], int(i["puertas"]), i["puertas"], float(i["precio_base"]), i["marca"], i["version"])
       else:
           unVehiculo = Usado(i["modelo"], int(i["puertas"]), i["puertas"], float(i["precio_base"]), i["marca"], i["patente"], int(i["anio"]), int(i["kilometraje"]) )
       lista.agregarVehiculo(unVehiculo)
        
        
def test():
    auto = Nuevo("Palio",4,"Rojo",100000,"porche","full")
    auto2 = Usado("Palio", 5, "Verde", 20000, "lambo", "ARESAD10", 2023, 0)
    concesionariaT = Lista()
    concesionariaT.agregarVehiculo(auto)
    concesionariaT.agregarVehiculo(auto2)
    concesionariaT.mostrarVehiculos()
    print("Finalizando Test...\n")
    

def mostrarMenu():
    print("|-------------------- MENÚ DE OPCIONES ---------------------|")
    print("| 1. Insertar un vehículo en una posición determinada       |")
    print("| 2. Agregar un vehículo a la lista                         |")
    print("| 3. Mostrar el tipo de objeto almacenado en una posición   |")
    print("| 4. Modificar precio de un vehículo usado y mostrarlo      |")
    print("| 5. Mostrar datos de los vehículo más económico            |")
    print("| 6. Mostrar datos de todos los vehículos en venta          |")
    print("| 7. Guardar datos de los vehiculos                         |")
    print("| 0. Finalizar Operacion                                    |")
    print("|-----------------------------------------------------------|")
    
    
def crearVehiculo():
    tipo = input("Ingrese el tipo de vehículo (nuevo/usado): ")
    modelo = input("Ingrese el modelo del vehículo: ")
    puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
    color = input("Ingrese el color del vehículo: ")
    precio = float(input("Ingrese el precio base del vehículo: "))
    marca = input("Ingrese la marca: ")

    if tipo.lower() == "nuevo":
        version = input("Ingrese la versión del vehículo (base/full): ")
        unvehiculo = Nuevo(modelo,puertas,color,precio,marca,version)
    else:
        marca = input("Ingrese la marca del vehículo usado: ")
        patente = input("Ingrese la patente del vehículo usado: ")
        anio = int(input("Ingrese el año del vehículo usado: "))
        kilometraje = float(input("Ingrese el kilometraje del vehículo usado: "))
        unvehiculo = Usado(modelo, puertas, color, precio_base, marca, patente, anio, kilometraje)  
    return unvehiculo  
    
if __name__=="__main__":
   #test()
   concesionaria = Lista()
   cargarVehiculos(concesionaria) #cargo los vehiculos que tengo en el archivo json
   #concesionaria.mostrarVehiculos() 
   mostrarMenu()
   op = str(input("Ingrese una opcion--> "))
   band = True
   while op != "0":
       
       if op == "1":
           posicion = int(input("Ingrese una posicion a insertar: "))
           vehiculo = crearVehiculo()
           concesionaria.agregarVehiculo(vehiculo)#########
           
       elif op == "2":
           vehiculo = crearVehiculo()
           concesionaria.agregarVehiculo(vehiculo)
           
       elif op == "3":
           posicion = int(input("Ingrese una posicion: "))
           print(concesionaria.buscarVehiculo(posicion))
           
       elif op == "4":
           patente = str(input("Ingrese una patente de un vehiculo: "))
           concesionaria.modificarPrecio(patente)
           
       elif op == "5":
           concesionaria.mostrarVehiculos()
             
       elif op == "6":
           concesionaria.mostrarVehiculos()
           
       elif op == "7":
           posicion = int(input("Ingrese una posicion: "))
           print(concesionaria.buscarVehiculo(posicion))
           
       elif op == "8":
           concesionaria.guardarDatosJson()
           
       elif op == "0":
           band = False
           
       if band:
          mostrarMenu()
          op = str(input("Ingrese otra opcion--> "))
           
