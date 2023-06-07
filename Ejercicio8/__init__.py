#   ********---UNIDAD 3 POO - Ejercicio8 - VB---*********

from abc import ABC, abstractmethod

# Interfaces
class ITesorero(ABC):
    @abstractmethod
    def gastosSueldoPorEmpleado(self, dni):
        pass

class IDirector(ABC):
    @abstractmethod
    def modificarBasico(self, dni, nuevoBasico):
        pass

    @abstractmethod
    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarPorcentajeporcategoría(self, dni, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass

# Implementación de las interfaces
class Tesorero(ITesorero):
    def gastosSueldoPorEmpleado(self, dni):
        pass

class Director(IDirector):
    def modificarBasico(self, dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoría(self, dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass


def autenticar_usuario():
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if usuario == "uTesoreria" and contraseña == "ag@74ck":
            return Tesorero()
        elif usuario == "uDirector" and contraseña == "ufC77#!1":
            return Director()
        else:
            print("Usuario o contraseña incorrectos. Por favor, intente nuevamente.")

def menu_tesorero(tesorero):
    dni = input("Ingrese el número de documento del empleado: ")
    tesorero.gastosSueldoPorEmpleado(dni)

def menu_director(director):
    dni = input("Ingrese el número de documento del empleado: ")
    opcion = input("Seleccione una opción:\n1. Modificar sueldo básico\n2. Modificar porcentaje por cargo\n3. Modificar porcentaje por categoría\n4. Modificar porcentaje extra\n")

    if opcion == "1":
        nuevo_basico = input("Ingrese el nuevo sueldo básico: ")
        director.modificarBasico(dni, nuevo_basico)
    elif opcion == "2":
        nuevo_porcentaje_cargo = input("Ingrese el nuevo porcentaje por cargo: ")
        director.modificarPorcentajeporcargo(dni, nuevo_porcentaje_cargo)
    elif opcion == "3":
        nuevo_porcentaje_categoria = input("Ingrese el nuevo porcentaje por categoría: ")
        director.modificarPorcentajeporcategoría(dni, nuevo_porcentaje_categoria)
    elif opcion == "4":
        nuevo_importe_extra = input("Ingrese el nuevo importe extra: ")
        director.modificarImporteExtra(dni, nuevo_importe_extra)
    else:
        print("Opción inválida")




if __name__ == "__main__":
        usuario_autenticado = autenticar_usuario()
        
        band = True
        while band:
            print("\nSeleccione una opción:")
            print("1. Tesorero")
            print("2. Director")
            print("3. Salir")
        
            opcion_principal = input()
        
            if opcion_principal == "1":
                menu_tesorero(usuario_autenticado)
            elif opcion_principal == "2":
                menu_director(usuario_autenticado)
            elif opcion_principal == "3":
                band = False
            else:
                print("Opción inválida")
        