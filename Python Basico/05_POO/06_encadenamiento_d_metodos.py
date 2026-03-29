class Coche:
    def encender(self):
        print('Has arrancado el motor')
        return self

    def conducir(self):
        print('Estas conduciendo el coche')
        return self

    def frenar(self):
        print('Estas frenando')
        return self

    def apagar(self):
        print('Has apagado el motor')
        return self

coche = Coche()

#coche.encender().conducir().frenar().apagar()

coche.encender()\
    .conducir()\
    .frenar()\
    .apagar()