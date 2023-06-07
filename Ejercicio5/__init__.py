#   ********---UNIDAD 3 POO - Ejercicio5 - VB---*********

from zope.interface import Interface
from zope.interface import implementer

class UnaInterfaz(Interface): #defino una interfaz 
        
    def insertarElemento(indice,elemento):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(indice):
       pass
   
@implementer(UnaInterfaz)   
class ManejadorLista:
    
    def __init__(self):
        self.__lista = []
        
    def insertarElemento(self,indice,elemento): #punto a
       assert indice <= len(self.__lista),"Indice fuera de rango"
       self.__lista.insert(indice-1,elemento)
    
    def agregarElemento(self,elemento): #punto b
        self.__lista.append(elemento)
        
    def mostrarElemento(self,indice): #punto c
        try:
            print("El elemento es: {}".format(self.__lista[indice-1]))
        except:
            print("Error, elemento a mostrar incorrecto!")
        else:
            print("No hubo errores")
        finally:
            print("Finalizando operacion...")
        
        
         
    def CargarAlgunosNumeros(self): #opcional
        num = 5
        for i in range(10):
            num+=i*3
            self.__lista.append(num)
            
    def mostrarElementos(self): #opcional
        for i in self.__lista:
            print(i)
        
    

#----------Programa Principal-----------------
if __name__ == "__main__":
   lista = ManejadorLista()
   lista.CargarAlgunosNumeros()
   lista.mostrarElementos()
   lista.insertarElemento(2,500)  #punto a
   #lista.insertarElemento(15,400)  #para realizar un error
   lista.agregarElemento(390) #punto b
   lista.mostrarElemento(1)   #punto c
   #lista.mostrarElementos() 