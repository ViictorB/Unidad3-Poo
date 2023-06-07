#   ********---UNIDAD 3 POO - Ejercicio4 - VB---*********
import csv
import numpy as np

#---------------------CLASES DEL DIAGRAMA-------------------------
#******    Clase Abstracta    *****
class Empleado(object):
    
    def __init__(self,nombre,dni,direc,tel):
        self.__nombre = nombre
        self.__dni = dni
        self.__direccion = direc
        self.__telefono = tel
        
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
        
    def mostrarDatos(self):
        print("Nombre {}     DNI {}".format(self.__nombre,self.__dni))
        print("Direccion {}   Telefono: {}".format(self.__direccion, self.__telefono))
        

#******    Clases Concretas (Clases hijas de la clase Empleados)    *****
class dePlanta(Empleado):
    
    def __init__(self,nomb,dni,direc,tel,sueldo,antig):
        super().__init__(nomb,dni,direc,tel)
        self.__sueldo = float(sueldo)
        self.__antiguedad = int(antig)
        
    def mostrarDatos(self):
        print("-------------------------------------------")
        super().mostrarDatos()
        print("Sueldo ${}   Antiguedad: {}años".format(self.__sueldo,self.__antiguedad))
        print("-------------------------------------------")
        
    def calcularSueldo(self):
        sueldo = (self.__sueldo + (self.__sueldo * 1/100) ) * self.__antiguedad
        #print("Sueldo: ${0:.2f}".format(sueldo))
        return sueldo
        
        
        
class contratados(Empleado):
    __valorPorHora = 500
    def __init__(self,nomb,dni,direc,tel,fechaI,fechaF,cant):
        super().__init__(nomb,dni,direc,tel)
        self.__fechaInicial = fechaI
        self.__fechaFinal = fechaF
        self.__cantHoras = int(cant)
        
    def mostrarDatos(self):
        print("-------------------------------------------")
        super().mostrarDatos()
        print("Fecha Inicial: {} - Fecha Final: {}".format(self.__fechaInicial,self.__fechaFinal))
        print("Horas Trabajadas: {} y su valor por hora es de: {}".format(self.__cantHoras,self.__valorPorHora))
        print("-------------------------------------------")
        
    def calcularSueldo(self):
        sueldo = self.__cantHoras * self.__valorPorHora
        #print("Sueldo: ${0:.2f}".format(sueldo))
        return sueldo
        
        
    def verificarEmpleado(self,dni):
        band = False
        if dni == super().getDni():
           band = True
        return band
    
    def setCantHoras(self,cant):
        self.__cantHoras = cant
   
class externos(Empleado):
    
    def __init__(self,nomb,dni,direc,tel,tarea,Fi,Ff,montoViat,costoObra,seguro):
        super().__init__(nomb,dni,direc,tel)
        self.__tarea = tarea
        self.__fechaInicial = Fi
        self.__fechaFinal = Ff
        self.__montoViatico = float(montoViat)
        self.__costoObra = float(costoObra)
        self.__segDeVida = float(seguro)
        
        
    def mostrarDatos(self):
        print("-------------------------------------------")
        super().mostrarDatos()
        print("Tarea que realiza/zo: {} ".format(self.__tarea.getNombre()))
        print("Fecha Inicial: {} - Fecha Final: {}".format(self.__fechaInicial,self.__fechaFinal))
        print("Monto Viatico: ${0:.2f}  costo de la Obra: ${0:.2f}".format(self.__montoViatico,self.__costoObra))
        print("Monto del seguro de vida: ${0:.2f}".format(self.__segDeVida))
        print("-------------------------------------------")
        
    def calcularSueldo(self):
        sueldo = self.__costoObra - self.__montoViatico - self.__segDeVida
        #print("Sueldo: ${0:.2f}".format(sueldo))
        return sueldo
        
    def verificarTarea(self,tarea):
        if self.__tarea.getNombre() == tarea:
            band = True
        else:
            band = False
        return band
    
    def mostrarMontoTarea(self):
        return self.__tarea.getMonto()
#-----------------------CLASES REQUERIDAS--------------------------    

class Tarea: #RELACION DE ASOCIACION con el empleado externo
    
    __cursando = True
    
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__empleado = None
        if nombre == "Electricidad":
            self.__monto = float(5000)
        elif nombre == "Carpinteria":
            self.__monto = float(4000)
        elif nombre ==  "Plomeria":
            self.__monto = float(3000)     
          
    def getNombre(self):
        return self.__nombre
    
    def setEmpleado(self,empleado):
        self.__empleado = empleado
        
    def setCursado(self):
        self.__cursando = False
        
    def getMonto(self):
        return self.__monto
    
#  ******     Manejador    ******

class Coleccion: #manejador de todos los empleados
    
    def __init__(self,dimension):
        self.__empleados = np.empty(dimension,dtype=Empleado)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = 5
        
    def addEmpleado(self,empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad] = empleado
        self.__cantidad+=1


#-----------------FUNCIONES---------------------

def cargarEmpDePlanta(empleados):
    band = True
    archivo = open("Activividades\Ejercicio4\planta.csv")
    reader = csv.reader(archivo,delimiter=";")
    for i in reader:
        if band:
            band = False
        else:
            unEmpleado = dePlanta(i[0],i[1],i[2],i[3],i[4],i[5])
            empleados.append(unEmpleado)
    archivo.close()
    
def cargarContratados(empleados):
    band = True
    archivo = open("Activividades\Ejercicio4\contratados.csv")    
    reader = csv.reader(archivo,delimiter=";")
    for i in reader:
        if band:
            band = False
        else:
            unEmpleado = contratados(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            empleados.append(unEmpleado)
    archivo.close()
    
def cargarExternos(empleados):
    band = True
    archivo = open("Activividades\Ejercicio4\externos.csv")
    reader = csv.reader(archivo,delimiter=";")
    for i in reader:
        if band:
            band = False
        else:
            tarea = Tarea(i[4])
            unEmpleado = externos(i[0],i[1],i[2],i[3],tarea,i[5],i[6],i[7],i[8],i[9])
            tarea.setEmpleado(unEmpleado)
            empleados.append(unEmpleado)
    archivo.close()
    
def cargarEmpleados(empleados,lista):
    for i in lista:
        empleados.addEmpleado(i)
        
def modificarHora(empleados):
    i = 0
    bandera  = True
    dni = str(input("Ingrese el Dni del empleado: "))
    cantHoras = int(input("Ingrese la cantidad de horas que trabajo en el dia de hoy: "))
    while i < len(empleados) and bandera:
        if empleados[i].verificarEmpleado(dni):
            bandera = False
            empleados[i].setCantHoras(cantHoras)
        i+=1
    if bandera:
        print("No se encontro ese Empleado")
    print()
            
def mostrarMontoTarea(empleados):
    i = 0
    band = True
    tarea = str(input("Ingrese el nombre de una Tarea: "))
    while i < len(empleados) and band:
        if empleados[i].verificarTarea(tarea):
            print("El monto de esa tarea es de: ${0:.2f}".format(empleados[i].mostrarMontoTarea()))
            band = False
        i+=1
    if band:
        print("No se encontro el nombre de esa Tarea")
    print()
    
def MostrarBenificiados(empl1,empl2,empl3):
    todos = empl1 + empl2 + empl3
    print("------- Empleados Benificiados por la Ayuda Economica por el Alberto XD --------")
    for i in todos:
        if i.calcularSueldo() < 150000:
            print("- Nombre: {} | DNI: {} | Direccion: {}".format(i.getNombre(), i.getDni(),i.getDireccion()))
    print("---------------------------------------------------------------------------------")
    print()
           
def CalcularSueldo(empl1,empl2,empl3):
    todos = empl1 + empl2 + empl3
    print("              --------------   Datos de Cobro   -----------------")
    for i in todos:
        print("- Nombre: {} | telefono: {} | Sueldo a Cobrar: ${}".format(i.getNombre(),i.getTelefono(),i.calcularSueldo()))
    print("                     ---------------------------------------------")
    
#-------------------Programa Principal---------------------    
if __name__ == "__main__":

    EmpDePlanta = []
    EmpContratados = []
    EmpExternos = []
    cargarEmpDePlanta(EmpDePlanta)
    cargarContratados(EmpContratados)
    cargarExternos(EmpExternos)
    
    # for i in EmpDePlanta:         #MOSTRAR LOS DATOS DE CADA TIPO DE EMPLEADOS (testing)
    #     i.mostrarDatos()
    # for i in EmpContratados:
    #     i.mostrarDatos()
    # for i in EmpExternos:
    #     i.mostrarDatos()
    
    print("Empleados: {}".format(len(EmpDePlanta)+len(EmpContratados)+len(EmpExternos))) #muestro la cant de empleados disponibles a registrar
    dimension = int(input("ingrese la cantidad de empleados a registrar: ")) #pido la dimension que tendra el arreglo(manejador)
    
    TotaldeEmpleados = Coleccion(dimension)  #Registro cada uno de los empleados en el manejador
    cargarEmpleados(TotaldeEmpleados,EmpDePlanta)
    cargarEmpleados(TotaldeEmpleados,EmpContratados)
    cargarEmpleados(TotaldeEmpleados,EmpExternos)
    
    modificarHora(EmpContratados) #Punto1 / modificar la cantidad de horas trabajadas de un empleado
    mostrarMontoTarea(EmpExternos) #Punto 2 / mostrar el monto de una determinada tarea 
    MostrarBenificiados(EmpDePlanta,EmpContratados,EmpExternos) #Punto 3 / muestro los datos de los empleados que cumple la condicion
    CalcularSueldo(EmpDePlanta,EmpContratados,EmpExternos) #Punto 4 / muestro los datos y los sueldos a cobrar de cada empleado
