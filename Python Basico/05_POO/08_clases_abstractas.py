from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def ir(self):
        pass
    def detener(self):
        pass

class Coche(Vehiculo):
    def ir(self):
        print('conduces el auto')

    def detener(self):
        print('El coche se esta deteniendo')

class Motocicleta(Vehiculo):
    def ir(self):
        print('andas en la moto')

    def detener(self):
        print('La motocicleta se esta deteniendo')

#vehiculo = Vehiculo()
coche = Coche()
motocicleta = Motocicleta()

#vehiculo.ir()
coche.ir()
coche.detener()
motocicleta.ir()
motocicleta.detener()
