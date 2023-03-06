class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, peso):
        super().__init__(color, ruedas)
        self.peso = peso
    
    def __str__(self):
        return super().__str__() + ", {} toneladas".format(self.peso)


c = Coche("azul", 4, 150, 1200)
print(c)

t = Camioneta("roja", 4, 1.5)
print(t)


