#   ********---UNIDAD 3 POO - Ejercicio7 - VB---*********

from zope.interface import interface
import json
from os import path

class Personal:
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self._cuil = cuil
        self._apellido = apellido
        self._nombre = nombre
        self._sueldo_basico = sueldo_basico
        self._antiguedad = antiguedad

    def __str__(self):
        return f"{self._apellido}, {self._nombre}"

class Docente(Personal):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self._carrera = carrera
        self._cargo = cargo
        self._catedra = catedra

class PersonalApoyo(Personal):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self._categoria = categoria

class Investigador(Personal):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self._area_investigacion = area_investigacion
        self._tipo_investigacion = tipo_investigacion

class DocenteInvestigador(Docente, Investigador):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria, importe_extra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        self._area_investigacion = area_investigacion
        self._tipo_investigacion = tipo_investigacion
        self._categoria = categoria
        self._importe_extra = importe_extra



class Lista:

    def _init_(self):
        
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def _iter_(self):

        self.__actual = self.__comienzo
        
        return self

    def _next_(self):
        
        if self.__actual is None:
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def crearAgente():
        
        agente = None
        
        print("Seleccione el tipo de agente que desea crear:")
        print("1. Docente")
        print("2. Investigador")
        print("3. Docente Investigador")
        print("4. Personal de Apoyo")
    
        tipo_agente = int(input("Ingrese el número correspondiente al tipo de agente: "))
    
        cuil = input("Ingrese el CUIL del agente: ")
        nombre = input("Ingrese el nombre del agente: ")
        apellido = input("Ingrese el apellido del agente: ")
        sueldo_basico = float(input("Ingrese el sueldo básico del agente: "))
        antiguedad = int(input("Ingrese la antigüedad del agente: "))

        if tipo_agente == 1:
        
            carrera = input("Ingrese la carrera del docente: ")
            cargo = input("Ingrese el cargo del docente: ")
            catedra = input("Ingrese la cátedra del docente: ")
            
            agente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
    
        elif tipo_agente == 2:
        
            area_investigacion = input("Ingrese el área de investigación: ")
            tipo_investigacion = input("Ingrese el tipo de investigación: ")
            
            agente = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
    
        elif tipo_agente == 3:
        
            carrera = input("Ingrese la carrera del docente investigador: ")
            cargo = input("Ingrese el cargo del docente investigador: ")
            catedra = input("Ingrese la cátedra del docente investigador: ")
            area_investigacion = input("Ingrese el área de investigación: ")
            tipo_investigacion = input("Ingrese el tipo de investigación: ")
            categoria_incentivos = input("Ingrese la categoría en el programa de incentivos de investigación: ")
            importe_extra = float(input("Ingrese el importe extra por docencia e investigación: "))
            
            agente = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        
        elif tipo_agente == 4:
            
            categoria = input("Ingrese la categoría del personal de apoyo: ")
            
            agente = PersonalApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
            
        else:
        
            print("Opción no válida.")
            return None

        return agente
    
    def agregarElemento(self, elemento):
        
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def insertarElemento(self, posicion, elemento):
        
        if not 0 <= posicion <= self.__tope:
            raise IndexError("Índice de posición fuera de rango")
        
        if posicion == 0:
            
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        
        else:
            
            nodo_anterior = None
            nodo_actual = self.__comienzo
            index = 0
            
            while index < posicion and nodo_actual is not None and posicion < self.__tope:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
                nodo = Nodo(elemento)
                nodo.setSiguiente(nodo_actual)
                nodo_anterior.setSiguiente(nodo)
        
        self.__tope += 1

        
    def mostrarElemento(self, posicion):
        
        if not 0 <= posicion < self.__tope:
            raise IndexError("Índice de posición fuera de rango")
        
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= posicion and nodo_actual is not None and posicion < self.__tope:
            
            if index == posicion:
                
                band = False
                print(nodo_actual)
            
            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
                
    def leerArchivoJSON(self, ruta_archivo):
    
        try:
            
            personal = None
            
            with open(ruta_archivo) as archivo:
            
                datos = json.load(archivo)
        
        except FileNotFoundError:
        
            print(f"El archivo no existe: {ruta_archivo}")
    
        except json.JSONDecodeError:
        
            print(f"El archivo no contiene datos JSON válidos: {ruta_archivo}")
        
        else:
            
            for dato in datos:
            
                tipo_personal = dato["tipo_personal"]
                cuil = dato["cuil"]
                apellido = dato["apellido"]
                nombre = dato["nombre"]
                sueldo_basico = dato["sueldo_basico"]
                antiguedad = dato["antiguedad"]
            
                if tipo_personal == "Docente":
                
                    carrera = dato["carrera"]
                    cargo = dato["cargo"]
                    catedra = dato["catedra"]
                    
                    personal = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
            
                elif tipo_personal == "Investigador":
                
                    area_investigacion = dato["area_investigacion"]
                    tipo_investigacion = dato["tipo_investigacion"]
                    
                    personal = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
            
                elif tipo_personal == "Docente_Investigador":
                
                    carrera = dato["carrera"]
                    cargo = dato["cargo"]
                    catedra = dato["catedra"]
                    area_investigacion = dato["area_investigacion"]
                    tipo_investigacion = dato["tipo_investigacion"]
                    categoria_incentivos = dato["categoria_incentivos"]
                    importe_extra = dato["importe_extra"]
                
                    personal = Docente_Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
            
                elif tipo_personal == "Personal_Apoyo":
                
                    categoria = dato["categoria"]
                    
                    personal = Personal_Apoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
                
                else:
                
                    print(f"Tipo de personal no válido: {tipo_personal}")
                
                self.agregarElemento(personal)
                
                
                
if __name__ == "__main__":
        
        lista = Lista()
        lista.leerArchivoJSON(path.dirname(__file__) + "personal.json")
        lista.mostrarElemento(2)
        
        print("1 - Insertar un agente en la colección en una posición determinada")
        print("2 - Agregar un agente a la colección")
        print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agentes se encuentra almacenado")
        print("4 - Punto 4")
        print("5 - Punto 5")
        print("6 - Punto 6")
        print("7 - Punto 7")
        print("8 - Almacenar los objetos de la colección Lista en el archivo “personal.json”")
        print("9 - Salir")
        
        op = input("Ingrese opción:")
        
        while(op != "9"):
            
            if op == "1":
                
                lista.insertarElemento(int(input("Ingrese posición:")),lista.crearAgente())
                
            elif op == "2":
                
                lista.agregarElemento(lista.crearAgente())
            
            elif op == "3":
                
                lista.mostrarElemento(int(input("Ingrese posición:")))


            print("1 - Insertar un agente en la colección en una posición determinada")
            print("2 - Agregar un agente a la colección")
            print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agentes se encuentra almacenado")
            print("4 - Punto 4")
            print("5 - Punto 5")
            print("6 - Punto 6")
            print("7 - Punto 7")
            print("8 - Almacenar los objetos de la colección Lista en el archivo “personal.json”")
            print("9 - Salir")

            op = input("Ingrese opción:")