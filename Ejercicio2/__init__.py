#   ********---UNIDAD 3 POO - Ejercicio2 - VB---*********
import csv

#----------------------------------------CLASES---------------------------------------------
class Helado:  #********Clase HELADO***********
    
    def __init__(self,gramos,precio):
       self.__gramos = int(gramos)
       self.__precio = float(precio)
       self.__sabores = []
       
    def getGramos(self):
        return self.__gramos   
    
    def getSabores(self):
        cadena = ""
        for i in self.__sabores:
            cadena += i.getNombreSabor()
            cadena += " / "
        return cadena
    def getPrecio(self):
        return self.__precio
       
    def addSabor(self,sabor):
        if len(self.__sabores) < 4:
            self.__sabores.append(sabor)
        else:
            print("Llego la cantidad maxima de sabores!")
            
    def __str__(self):
        sabores = ""
        for i in self.__sabores:
            sabores += i.getNombreSabor() + " / "
        cadena = "Sabor/es Pedido: " + sabores
        cadena += "\nPrecio: $"+ str(self.__precio) + "   de " +str(self.__gramos)+"gr"
        return cadena
        
                  
class Sabor: #***********Clase SABOR*************

    def __init__(self,idSabor,sabor,ingredientes):
        self.__idSabor = idSabor
        self.__nombreSabor = sabor
        self.__ingredientes = ingredientes
        
    def getNombreSabor(self):
        return self.__nombreSabor
    
        
class ManejadorSabores: #***********Registro los Sabores de la Heladeria**********
    
    def __init__(self):
        self.__sabores = []
        self.__contadorSabores = [0,0,0,0,0,0,0,0,0,0] #contador de cantidad de sabores vendidos
        
    def cargarSabores(self):
        archivo = open("Activividades\\Ejercicio2\\sabores.csv")
        reader = csv.reader(archivo,delimiter=";")
        for i in reader:
            unsabor = Sabor(int(i[0]),i[1],i[2])
            self.__sabores.append(unsabor)
        archivo.close()
        
    def pedirSabor(self,idSabor):
        self.__contadorSabores[idSabor-1] += 1 #aumento en 1 el sabor pedido
        return self.__sabores[idSabor-1]
    
    def mostrarSaboresVendidos(self): #*******PUNTO 2*******
        listaAux = self.__contadorSabores.copy() #Si o si tenia que hacer una copia auxiliar
        print("Sabores Mas vendidos:")
        for j in range(5):
            max = 0
            for i in range(len(listaAux)):
                if listaAux[i] > max:
                    max = listaAux[i]
                    indice = i
            listaAux[indice] = -1
            print("{} - Sabor: {}".format(j+1, self.__sabores[indice].getNombreSabor()))
             
        

class ManejadorHelado:  #**************Registro la Venta de Helados**************
    
    def __init__(self):
        self.__HelVendidos = []
        
    def venderHelado(self,helado):
        self.__HelVendidos.append(helado)
        
    def mostrarVentas(self): #muestro los datos de los helados vendidos "punto 3 xd"
        for i in self.__HelVendidos:
            print(i)
            
    def mostrarHelVendSegunTipo(self, tipo):  #*****PUNTO 4*****
        if tipo in [100,150,250,500,1000]: #si es uno de estos tipo de helados entra
            cont = 0
            for i in self.__HelVendidos:
                if i.getGramos() == tipo:
                    cont+=1
                    print("{} - Sabores: {}".format(cont,i.getSabores()))
        else:
            print("Tipo de Helado Incorrecto!")
            
    def mostrarImporteTotal(self):   #********PUNTO 5*******
        acum = 0
        for i  in self.__HelVendidos:
            acum += i.getPrecio()
        print("Monto total recaudado: ${0:.2f}".format(acum))
        
        
            
#----------------------------------------FUNCIONES------------------------------------------------ 

def test(sabores,registroVentas):   #**************Test del Programa*****************
    
    helado1 = Helado(150,300)              #Pido un helado
    helado1.addSabor(sabores.pedirSabor(6)) #agrego sabor...
    helado2 = Helado(500,800)              #Pido otro helado
    helado2.addSabor(sabores.pedirSabor(2)) #agrego sabores
    helado2.addSabor(sabores.pedirSabor(2))
    helado2.addSabor(sabores.pedirSabor(5))
    helado3 = Helado(250,500)              #Pido otro helado
    helado3.addSabor(sabores.pedirSabor(1)) #agrego los sabores
    helado3.addSabor(sabores.pedirSabor(5))
    helado3.addSabor(sabores.pedirSabor(5))
    helado4 = Helado(1000,1250)            #Pido otro helado
    helado4.addSabor(sabores.pedirSabor(1)) #agrego sabores
    helado4.addSabor(sabores.pedirSabor(5))
    helado4.addSabor(sabores.pedirSabor(9))
    helado4.addSabor(sabores.pedirSabor(8))
    helado5 = Helado(1000,1250)            #Pido otro helado
    helado5.addSabor(sabores.pedirSabor(6)) #agrego sabores
    helado5.addSabor(sabores.pedirSabor(9))
    helado5.addSabor(sabores.pedirSabor(3))
    helado5.addSabor(sabores.pedirSabor(4))
    registroVentas.venderHelado(helado1)   #registro la venta de los helados pedidos
    registroVentas.venderHelado(helado2)
    registroVentas.venderHelado(helado3)
    registroVentas.venderHelado(helado4)
    registroVentas.venderHelado(helado5)
    
    
def mostrarMenu(): #**********Mostrar el Menu de Opciones**************
    print()
    print("****************MENU DE OPCIONES****************")
    print("1 - Registrar Helado") 
    print("2 - Mostrar los 5 Sabores Mas vendidos")
    print("3 - Mostrar gramos vendidos de un sabor")
    print("4 - Mostrar sabores vendidos de un tipo de helado")
    print("5 - Mostrar Importe Total Recaudado")   
    print("0 - Finalizar Operacion!")
    print("************************************************")

def registrarHelado(sabores,registroVentas):  #*******PUNTO 1*******
    band = True #por si no eligio bien el tipo de helado
    tipo = int(input("Ingrese el tipo de Helado: "))  
    if tipo == 100:
        helado = Helado(tipo,200) #creo la instancia de helado con su respectivo precio
    elif tipo == 150:
        helado = Helado(tipo,300)
    elif tipo == 250:
        helado = Helado(tipo,500)
    elif tipo == 500:
        helado = Helado(tipo,800)
    elif tipo == 1000:
        helado = Helado(tipo,1250)
    else:
        print("Tipo de Helado Incorrecto")
        band = False
        
    if band:
        opsabor = int(input("Seleccione los sabores: '1 - 10': ")) #selecciono los sabores
        if opsabor > 0 and opsabor < 11:
           helado.addSabor(sabores.pedirSabor(opsabor))
           print("Sabor Agregado!")
           while opsabor != 0: #para agregar mas sabores
               opsabor = int(input("Seleccione otro sabor a agregar o finalice con 0: "))
               if opsabor > 0 and opsabor < 11:
                   helado.addSabor(sabores.pedirSabor(opsabor))
                   print("Sabor Agregado!")
               elif opsabor == 0:
                   print()
               else:
                   print("Id de sabor incorrecto!")
           registroVentas.venderHelado(helado)
           print("Venta registrada con exito!")

def MenuDeOpciones(op,sabores,registroVentas):
    while op != "0":
        if op == "1":
           registrarHelado(sabores,registroVentas) #Registro la venta de un helado 
        elif op == "2":
            sabores.mostrarSaboresVendidos() #Muestro los nombres de los sabores mas pedidos
        elif op == "3": 
            registroVentas.mostrarVentas() #NADA QUE VER PERO MUESTRO TODAS LAS VENTAS  :C "Me falta este punto nomas"
        elif op == "4":
            tipo = int(input("Ingrese un tipo de Helado (100gr - 150gr - 250gr - 500gr - 1000): "))
            registroVentas.mostrarHelVendSegunTipo(tipo) #Mustro todas las ventas de un tipo de helado
        elif op == "5":
            registroVentas.mostrarImporteTotal()
        else:
            print("Opcion Incorrecta!")
        mostrarMenu()
        op = str(input("Ingrese una nueva opcion---> "))
    print("Finalizando Operacion......")
    


#-----------------------PROGRAMA PRINCIPAL-------------------------
if __name__ == "__main__":
    
    sabores = ManejadorSabores() #creo la lista de sabores
    sabores.cargarSabores() #cargo los sabores
    registroVentas = ManejadorHelado() #creo la lista de registro de ventas
    
    test(sabores,registroVentas) #cargo algunos helados
    
    mostrarMenu() 
    op = str(input("Ingrese una Opcion---> "))
    MenuDeOpciones(op,sabores,registroVentas)
    
    