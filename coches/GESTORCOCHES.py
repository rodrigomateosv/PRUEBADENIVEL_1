import configuracion
import csv


class Vehiculo(): 
    def __init__(self,ID, color, ruedas):
        self.ID = ID
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "ID {},color {}, {} ruedas".format(self.ID,self.color, self.ruedas)
    def to_dict(self): 
        return {'ID': self.ID, 'color': self.color, 'ruedas': self.ruedas}


class Coche(Vehiculo):
    def __init__(self,ID, color, ruedas, velocidad, cilindrada):
        super().__init__(ID,color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    def to_dict(self):
        return super().to_dict()+ {'velocidad':self.velocidad,'cilindrada':self.cilindrada}



class Camioneta(Coche):
    def __init__(self,ID, color, ruedas,velocidad,cilindrada, peso):
        super().__init__(ID,color, ruedas, velocidad, cilindrada)
        self.peso = peso
    
    def __str__(self):
        return super().__str__() + ", {} toneladas".format(self.peso)
    def to_dict(self):
        return super().to_dict()+ {'peso':self.peso}
    
class F1(Coche):
    def __init__(self,ID, color, ruedas,velocidad,cilindrada, escuderia):
        super().__init__(ID,color, ruedas, velocidad, cilindrada)
        self.escuderia = escuderia
    
    def __str__(self):
        return super().__str__() + ", {} ".format(self.escuderia)
    def to_dict(self):
        return super().to_dict()+ {'escuderia':self.escuderia}

class Bicicleta(Vehiculo):
    def __init__(self,ID, color, ruedas, tipo):
        super().__init__(ID,color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", tipo {}".format(self.tipo)
    def to_dict(self):
        return super().to_dict()+ {'tipo':self.tipo}


class Motocicleta(Bicicleta):
    def __init__(self,ID, color, ruedas,tipo, velocidad, cilindrada):
        super().__init__(ID,color, ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    def to_dict(self):
        return super().to_dict()+ {'velocidad':self.velocidad,'cilindrada':self.cilindrada}
    
    
    
class Quad(Coche,Bicicleta):
    def __init__(self,ID, color, ruedas,velocidad,cilindrada, tipo,modelo='',carga=0):
        super().__init__(ID,color, ruedas, velocidad, cilindrada, tipo)
        self.modelo = modelo
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + f", {self.modelo}, {self.carga} kilos" 
    def to_dict(self):
        return super().to_dict()+ {'modelo':self.modelo,'carga':self.carga}
    


class Vehiculos():
    lista = []
    with open(configuracion.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for ID, color, ruedas, velocidad, cilindrada, tipo, modelo, carga, escuderia in reader:
            if tipo == "coche":
                vehiculo = Coche(ID, color, ruedas, velocidad, cilindrada)
            if tipo == "bicicleta":
                vehiculo = Bicicleta(ID, color, ruedas, tipo)
            if tipo == "camioneta":
                vehiculo = Camioneta(ID, color, ruedas, velocidad, cilindrada, carga)
            if tipo == "fórmula1":
                vehiculo = F1(ID ,color ,ruedas ,velocidad ,cilindrada ,escuderia ) 
            if tipo == "motocicleta": 
                vehiculo = Motocicleta(ID ,color ,ruedas ,tipo ,velocidad ,cilindrada ) 
            if tipo == "quad": 
                vehiculo = Quad(ID ,color ,ruedas ,velocidad ,cilindrada ,tipo ,modelo ,carga ) 

            lista.append(vehiculo)


    @staticmethod
    def catalogar():
        for vehiculo in Vehiculos.lista:
            print("{} {}".format(type(vehiculo).__name__, vehiculo))
    @staticmethod
    def buscar(ID):
        for vehiculo in Vehiculos.lista:
            if vehiculo.ID == ID:
                return vehiculo

    @staticmethod
    def crear(ID, color, ruedas):
        vehiculo = vehiculo(ID, color, ruedas)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo

    @staticmethod
    def modificar(ID, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.ID == ID:
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.lista[indice]

    @staticmethod
    def borrar(ID):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.ID == ID:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(configuracion.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                writer.writerow((vehiculo.ID, vehiculo.color, vehiculo.ruedas))














