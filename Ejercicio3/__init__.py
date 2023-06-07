#   ********---UNIDAD 3 POO - Ejercicio3 - VB---*********
import csv
import numpy as np

#--------------------CLASES (del diagrama)--------------------------
class Persona:
    
    def __init__(self,nom,dni,direc):
        self.__nombre = nom
        self.__dni = dni
        self.__direccion = direc
        
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getDireccion(self):
        return self.__direccion
    
    def __str__(self):
        cadena = "-----------------------------------------\n"
        cadena += "Nombre: "+ self.__nombre + "    DNI: "+ self.__dni
        cadena +="\nDireccion: " + self.__direccion
        cadena += "\n-----------------------------------------"
        return cadena
      
class TallerCapacitacion:
    
    def __init__(self,idTaller,nombre,vacantes,monto):
        self.__idTaller = idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = monto
        self.__inscripciones = []
   
    def getIdTaller(self):
       return self.__idTaller
    def getNombre(self):
        return self.__nombre
    def getVacantes(self):
        return self.__vacantes
    def getMontoInscripcion(self):
       return self.__montoInscripcion
    
    def actualizarVacante(self):
        self.__vacantes-=1
        
    def addInscripcion(self,inscripcion):
        self.__inscripciones.append(inscripcion)
        
    def mostrarInscripciones(self):
        for i in self.__inscripciones:
            i.mostrarDatos()
            
        
class Inscripcion:
    
    def __init__(self,fecha,pago,persona,taller):
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller
        
    def getFecha(self):
        return self.__fecha
    def getPago(self):
        return self.__pago
    def getPersona(self):
        return self.__persona
    def getTaller(self):
        return self.__taller
    def setPago(self):
        self.__pago = True
    
    def verificarInscripto(self,dni):
        band: bool
        if self.__persona.getDni() == dni:
            band = True
        else:
            band = False
        return band
    
    def mostrarTaller(self):
        return self.__taller.getNombre()
    
    def mostrarMonto(self):
        return self.__taller.getMontoInscripcion()
    
    def mostrarDatos(self):
        print(self.__persona)
        
    def getDniPersona(self):
        return self.__persona.getDni()
    
    def getId(self):
        return self.__taller.getIdTaller()

        
        
#--------------------CLASES (manejadores)--------------------------
class ManejadorTalleres: #Manejador de los talleres con un arreglo

    def __init__(self,dimension):
        self.__talleres = np.empty(dimension,dtype=TallerCapacitacion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = 5

    def cargarTalleres(self):
       band = True
       archivo = open("Activividades\\Ejercicio3\\Talleres.csv")
       reader = csv.reader(archivo,delimiter=";")
       for i in reader:
           if band:
                band = False
           else:
            untaller = TallerCapacitacion(int(i[0]),i[1],int(i[2]),i[3])
            if self.__cantidad == self.__dimension:
                self.__dimension+=self.__incremento
                self.__talleres.resize(self.__dimension)
            self.__talleres[self.__cantidad]=untaller
            self.__cantidad += 1
       archivo.close()
            
    def inscribir(self,idTaller,persona,inscripciones,fecha):
        band = 0
        if idTaller <= len(self.__talleres) and idTaller != 0:
           if self.__talleres[idTaller - 1].getVacantes() != 0:
               inscripcion = Inscripcion(fecha,False,persona,self.__talleres[idTaller-1])
               self.__talleres[idTaller - 1].addInscripcion(inscripcion)
               inscripciones.agregarInscripcion(inscripcion)
               band = 1
        else: band = -1
        return band
        
    def actualizarVacante(self,idTaller):
        self.__talleres[idTaller-1].actualizarVacante()
        
    def listarInscriptos(self,idTaller): 
        if idTaller > 0 and idTaller <= self.__cantidad:
            self.__talleres[idTaller-1].mostrarInscripciones()
        else:
            print("Numero de Taller Incorrecto!")
    
       

class ManejadorPersonas:
    
   def __init__(self):
       self.__personas = []
    
   def cargarPersona(self,persona):
       self.__personas.append(persona)
       
   def mostrarPersonas(self):
        for i in self.__personas:
            print(i.getNombre())
            
            
class ManejadorInscripciones:
    
    def __init__(self,dimension = 15):
        self.__inscripciones = np.empty(dimension, dtype=Inscripcion)
        self.__dimension = dimension
        self.__cantidad = 0
        self.__incremento = 5
        
    def agregarInscripcion(self,inscripcion):
       if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripciones.resize(self.__dimension)
       self.__inscripciones[self.__cantidad] = inscripcion
       self.__cantidad += 1

    def consultarInscripto(self,dni):
        band = True
        i = 0
        while i < self.__cantidad and band:
            if self.__inscripciones[i].verificarInscripto(dni):
                print("Taller en el que se inscribio: {}".format(self.__inscripciones[i].mostrarTaller()))
                print("Monto adeudado: ${}".format(self.__inscripciones[i].mostrarMonto()))
                band = False
            i+=1
        if band:
            print("No se encuentra registrado en ninguno curso!")
            
    def registrarElPago(self,dni):
        band = True
        i = 0
        while i < self.__cantidad and band:
            if self.__inscripciones[i].verificarInscripto(dni):
                self.__inscripciones[i].setPago()
                print("Registro de Pago con exito!")
                band = False
            i+=1
        if band:
            print("No se encontro el Dni ingresado!")
                
    def getInscripciones(self):
       lista = []
       for i in range(self.__cantidad): #por cada inscripcion 
           dni = str(self.__inscripciones[i].getDniPersona())
           idTaller = int(self.__inscripciones[i].getId())
           fecha = self.__inscripciones[i].getFecha()
           pago = self.__inscripciones[i].getPago()
           lista.append([dni,idTaller,fecha,pago])  #agrego todo en una misma fila
       #lista = [["dni1","idTaller1","fecha1","pago1"], ["dni2","idTaller2","fecha2","pago2"]]
       return lista
       
            

#----------------------FUNCIONES-------------------------
def test(talleres,personas,inscripciones): #cargar algunos datos 
    
    persona1 = Persona("Marcos", "43888555", "Calle Superiora 150 - Rawson")
    persona2 = Persona("Mariana", "42999678", "Mendoza Sur 117 - Capital")
    persona3 = Persona("Julieta", "45677111", "Ignacio De la Rosa 1009 - Rivadavia")
    persona4 = Persona("Lionel", "40101100", "Calle 11 - Pocito")
    personas.cargarPersona(persona1)
    personas.cargarPersona(persona2)
    personas.cargarPersona(persona3)
    personas.cargarPersona(persona4)
    talleres.inscribir(1,persona1,inscripciones,"21/05/23")
    talleres.inscribir(1,persona2,inscripciones,"22/05/23")
    talleres.inscribir(5,persona3,inscripciones,"22/05/23")
    talleres.inscribir(6,persona4,inscripciones,"25/05/23")
    talleres.actualizarVacante(1)
    talleres.actualizarVacante(1)
    talleres.actualizarVacante(5)
    talleres.actualizarVacante(6)
    

def InscribirUnaPersona(talleres,personas,inscripciones): #funcion del punto 2
    print("-----Proceso de Inscripcion-----")
    nombre = str(input("Ingrese el nombre de la persona a escribir: "))
    dni = str(input("Dni: "))
    direccion = str(input("Direccion: "))
    idTaller = int(input("Ingrese el numero del taller que desea Inscribirse '1 - 12' : "))
    unaPersona = Persona(nombre,dni,direccion) 
    
    bandera = talleres.inscribir(idTaller,unaPersona,inscripciones,"20/05/23") #realizo la inscripcion en el manejaroTaller
    if bandera == 1:
        personas.cargarPersona(unaPersona) #cargo la persona en el manejadorPersonas
        talleres.actualizarVacante(idTaller) #actualizo la vacante del taller
        print("Persona Inscripta con exito!")
    elif bandera == 0:
        print("No hay Vacantes suficientes para ese taller")
    elif bandera == -1:
        print("Numero de Taller Incorrecto!")
        

def consultarInscripcion(talleres,personas,inscripciones): #funcion del punto 3
    print("\n------Consultar Inscripcion------")
    dni = str(input("Ingrese el DNI de una persona: "))
    inscripciones.consultarInscripto(dni)
    

def consultarInscriptos(talleres): #funcion del punto 4
    print("\n------Consultar Inscriptos--------")
    idtaller = int(input("Ingrese el numero del Taller para ver los inscriptos: "))
    talleres.listarInscriptos(idtaller)
    

def registrarPago(inscripciones):
    print("\n------Registrar Pago--------")
    dni = str(input("Ingrese el Dni de la persona que realizo el pago: "))
    inscripciones.registrarElPago(dni)


def GuardarInscripciones(inscripciones):
    with open("Activividades\Ejercicio3\inscripciones.csv", "w" , newline= "") as archivo:
        writer = csv.writer(archivo, delimiter=";")
        writer.writerows(inscripciones.getInscripciones())
    archivo.close()
    print("Inscripciones Guardadas en el archivo con exito!")
    

#-----------------------Programa Principal---------------------------
if __name__ == "__main__":
    
    talleres = ManejadorTalleres(12)  #creo un manejador que tendra n TALLERES "n = 12 en este ejemplo" 
    personas = ManejadorPersonas()    #manejador de TODAS las PERSONAS inscriptas
    inscripciones = ManejadorInscripciones() #manejador de TODAS las INSCRIPCIONES realizadas
    
    talleres.cargarTalleres() #punto 1 / cargo del archivo los datos de los talleres  (12)
    test(talleres,personas,inscripciones) #Cargo cuatro personas para tener algunos datos ya cargados (inscriptas)
    
    InscribirUnaPersona(talleres,personas,inscripciones) #punto 2 / inscribir una persona a un determinado taller
    consultarInscripcion(talleres,personas,inscripciones) #punto 3 / consultar si una persona esta inscripta en algun taller
    consultarInscriptos(talleres) #punto 4 / listar personas que se inscribieron en un taller
    registrarPago(inscripciones) #punto 5 / registrar que una persona ya pago el importe del taller 
    GuardarInscripciones(inscripciones) #Punto 6 / Guardar en un archivo csv las inscripciones realizadas