#   ********---UNIDAD 3 POO - Ejercicio9 - VB---*********

class TestConcesionaria:
    def __init__(self):
        self.concesionaria = Concesionaria() 

    def probarTest(self):
        self.test_insertar_en_posicion_0()
        self.test_insertar_en_posicion_intermedia()
        self.test_insertar_en_ultima_posicion()
        self.test_agregar_vehiculo()
        self.test_obtener_objeto_en_posicion()
        self.test_modificar_precio_venta()

    def test_insertar_en_posicion_0(self):
        vehiculo1 = VehiculoNuevo("Palio", 4, "Rojo", 20000, "base", "Fiat")
        vehiculo2 = VehiculoNuevo("Focus", 5, "Azul", 25000, "full", "Ford")

        self.concesionaria.insertar_vehiculo(vehiculo1, 0)
        self.concesionaria.insertar_vehiculo(vehiculo2, 0)

        # Verificar el estado final de la lista
        assert self.concesionaria.vehiculos[0] == vehiculo2
        assert self.concesionaria.vehiculos[1] == vehiculo1

    def test_insertar_en_posicion_intermedia(self):
        vehiculo3 = VehiculoUsado("Gol", 3, "Blanco", 15000, "Volkswagen", "ABC123", 2015, 80000)
        vehiculo4 = VehiculoUsado("Clio", 3, "Gris", 12000, "Renault", "XYZ987", 2010, 120000)

        self.concesionaria.insertar_vehiculo(vehiculo3, 1)
        self.concesionaria.insertar_vehiculo(vehiculo4, 1)

        # Verificar el estado final de la lista
        assert self.concesionaria.vehiculos[0] == vehiculo2
        assert self.concesionaria.vehiculos[1] == vehiculo4
        assert self.concesionaria.vehiculos[2] == vehiculo3
        assert self.concesionaria.vehiculos[3] == vehiculo1

    def test_insertar_en_ultima_posicion(self):
        vehiculo5 = VehiculoNuevo("Civic", 4, "Negro", 35000, "full", "Honda")

        self.concesionaria.insertar_vehiculo(vehiculo5, len(self.concesionaria.vehiculos))

        # Verificar el estado final de la lista
        assert self.concesionaria.vehiculos[-1] == vehiculo5

    def test_agregar_vehiculo(self):
        vehiculo6 = VehiculoUsado("Corsa", 5, "Rojo", 10000, "Chevrolet", "DEF456", 2008, 150000)

        self.concesionaria.agregar_vehiculo(vehiculo6)

        # Verificar el estado final de la lista
        assert self.concesionaria.vehiculos[-1] == vehiculo6

    def test_obtener_objeto_en_posicion(self):
        vehiculo7 = VehiculoUsado("Yaris", 5, "Plata", 14000, "Toyota", "GHI789", 2013, 90000)

        self.concesionaria.agregar_vehiculo(vehiculo7)

        # Obtener un objeto de la lista en una posición determinada
        objeto_obtenido = self.concesionaria.obtener_objeto_en_posicion(1)

        # Verificar que el objeto obtenido sea el que está en la posición
        assert objeto_obtenido == vehiculo7

    def test_modificar_precio_venta(self):
        vehiculo8 = VehiculoUsado("Fiesta", 3, "Plata", 18000, "Ford", "JKL123", 2012, 70000)

        self.concesionaria.agregar_vehiculo(vehiculo8)

        patente = "JKL123"
        nuevo_precio_base = 20000

        self.concesionaria.modificar_precio_base(patente, nuevo_precio_base)

        # Obtener el precio de venta del vehículo modificado
        precio_venta = self.concesionaria.calcular_precio_venta(patente)

        # Verificar el nuevo precio de venta
        assert precio_venta == (nuevo_precio_base - (nuevo_precio_base * 0.01 * (2023 - vehiculo8.anio)))



if __name__ == "__main__":
    test = TestConcesionaria()
    test.probarTest() #llamando este metodo realizo el test