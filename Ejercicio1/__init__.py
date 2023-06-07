#   ********---UNIDAD 3 POO - Ejercicio1 - VB---*********
import csv

#CLASE FACULTAD (todo)
class Facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carreras = []
    
    def __init__(self,cod,nom,direc,loc,tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = direc
        self.__localidad = loc
        self.__telefono = tel
        self.__carreras = []
        
    def addCarrera(self,carrera,indice):
        if indice == 0:
            self.__carreras.append(carrera)
        else:
            self.__carreras.insert(indice,carrera)
        
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__codigo
    def getLocalidad(self):
        return self.__localidad
    
    def mostrarCarreras(self):
        print()
        print("-------Carreras--------")
        for i in self.__carreras:
            print("{}    {}".format(i.getNombre(), i.getDuracion()))
        print("-----------------------")
    
    def buscarCarrera(self,nom):
        aux = "0"
        for i in self.__carreras:
            if i.getNombre() == nom:
                aux = i.getNombre()
        return aux
        
    def getCodigoCarrera(self,nomb):
        codigo = "0"
        for i in self.__carreras:
            if i.getNombre() == nomb:
                codigo = i.getCodigo()
        return codigo
    
    def calcular(self): #test
        cant = 0
        for i in self.__carreras:
            if isinstance(i, Carrera): #verifico las intancias de la clase carrera 
                cant += 1 
        return cant
             
#CLASE CARRERA (parte)
class Carrera:
    __codigo: int
    __nombre: str
    __fechaInicio: str
    __duracion: str
    __titulo: str
    
    def __init__(self,cod,nom,fecha,dur,tit):
        self.__codigo = cod
        self.__nombre = nom
        self.__fechaInicio = fecha
        self.__duracion = dur
        self.__titulo = tit
        
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getCodigo(self):
        return self.__codigo
        
class ManejaFacultades: #MANEJO LAS 5 FACULTADES ATRAVEZ DE ESTA LISTA

    def __init__(self):
       self.__facultades = []
       
    # def cargarDatos(self):   #NOSE PORQUE DE ESTA FORMA ME CARGABA TODAS LAS INSTANCIAS CARRERA EN TODAS LAS FACULTADES
    #     archivo = open("Activividades\\Ejercicio1\\facultades.csv")
    #     reader = csv.reader(archivo,delimiter=",")
    #     band = True
    #     j = int(0)
    #     for i in reader:
    #         if band:
    #            facultad = Facultad(int(i[0]),i[1],i[2],i[3],i[4])
    #            cod = int(i[0])
    #            self.__facultades.append(facultad)
    #            band = False
    #         else:
    #             if cod == int(i[0]):
    #                 carrera = Carrera(int(i[1]),i[2],i[3],i[4],i[5])
    #                 self.__facultades[j].addCarrera(carrera)
    #             else:
    #                 j+=1
    #                 cod = int(i[0])
    #                 facultad = Facultad(int(i[0]),i[1],i[2],i[3],i[4])
    #                 self.__facultades.append(facultad)
    #     print("Datos cardados con exito!")
    #     archivo.close()
    
    def cargarDatos(self):  #CARGO LOS DATOS de esta forma
        archivo = open("Activividades\\Ejercicio1\\facultades.csv")
        reader = csv.reader(archivo,delimiter=",")
        band = True
        j = int(0)
        for i in reader:
            if band:
               facultad = Facultad(int(i[0]),i[1],i[2],i[3],i[4])
               cod = int(i[0])
               self.__facultades.append(facultad)
               band = False
            else:
                if cod == int(i[0]):
                    carrera = Carrera(int(i[1]),i[2],i[3],i[4],i[5])
                    self.__facultades[j].addCarrera(carrera,j)
                else:
                    j+=1
                    cod = int(i[0])
                    facultad = Facultad(int(i[0]),i[1],i[2],i[3],i[4])
                    self.__facultades.append(facultad)
        print("Datos cardados con exito!")
        archivo.close()


        
    def mostrarDatosFacultad(self,cod):
        if cod >= 1 and cod <= 5:
            print(self.__facultades[cod-1].getNombre())
            self.__facultades[cod-1].mostrarCarreras()
        else:
            print("Codigo de Facultad Incorrecto!")
       
    def mostrarDatosCarreras(self, nomb): #####
        i = self.__facultades
        j = int(0) #para ir cambiando de facultades
        band = True #para frenar el while una vez que encuentre la carrera de una facultad
        while j < len(i) and band == True:
            nombre = i[j].buscarCarrera(nomb)
            if nombre!= "0":
                print("Codigo de Facultad: {}   Codigo de Carrera: {}".format(i[j].getCodigo(),i[j].getCodigoCarrera(nombre)))
                print("{}  localizada en: {}".format(i[j].getNombre(),i[j].getLocalidad()))
                band = False
            j+=1
        if band == True: #por si no encontro la carrera
            print("No se encuentra registrada la carrera ingresada!")
            
    def verificar(self): #Verificar Instancias (test) #################################################
        j = 1
        for i in self.__facultades:
            print("Intancias de Clase Carrera de la facultad {} son: {} ".format(j,i.calcular()))
            j+=1
       
       
       
       
def mostrarMenu():
    print()
    print("*************MENU*************")   
    print("1 - Mostrar Facultad y las carreras que se dictan")    
    print("2 - Mostrar datos de una determinada carrera")
    print("0 - Finalizar Operacion")
    print("*******************************")
       
       
def menuDeOpciones(facultades):
   mostrarMenu()
   op = str(input("Ingrese una opcion--> "))   
   while op != "0":
       if op == "1":
           cod = int(input("Ingrese un codigo de facultad '1 - 5': "))
           facultades.mostrarDatosFacultad(cod)
       elif op == "2":
           NombreCarrera = str(input("Ingrese una carrera: "))
           facultades.mostrarDatosCarreras(NombreCarrera)  
       elif op == "3": #para verificar las intancias de las carreras (test)
           facultades.verificar()
       else:
           print("Opcion Incorrecta!")
           
       mostrarMenu()
       op = str(input("Ingrese una nueva opcion--> "))
   print("Finalizando operacion...")
          
       
if __name__ == "__main__":
    facultades = ManejaFacultades()
    facultades.cargarDatos()
    menuDeOpciones(facultades)
        
    