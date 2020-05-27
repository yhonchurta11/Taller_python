class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindraje):
        super().__init__(color, ruedas)  
        self.velocidad = velocidad
        self.cilindrada = cilindraje

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada)


class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Moto(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindraje

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada) 


def catalogar(vehiculos, ruedas=None):

    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)


lista = [
    
    Coche("negro", 0, 145, 1100),
    Bicicleta("roja", 2, "urbana"),
    Camioneta("blanca", 4, 120, 1250, 1400),
    Moto("azul", 3, "deportiva", 220, 700)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)
