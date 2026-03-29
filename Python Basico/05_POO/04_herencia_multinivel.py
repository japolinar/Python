class Organismo :
    vivo = True

class Animal(Organismo):
    def comer(self):
        print('El animal esta comiendo')

class Perro(Animal):
    def ladrar(self):
        print('El perro esta ladrando')

perro = Perro()

print(perro.vivo)
perro.ladrar()
perro.comer()
