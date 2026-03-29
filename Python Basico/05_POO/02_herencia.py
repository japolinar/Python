class Animal:

    vivo = True

    #importante colocar (self)
    def comer(self):
        print('Esta comiendo')

    def dormir(self):
        print('Esta durmiendo')

class Conejo(Animal):
    def correr(self):
        print('Corriendo')

class Pez(Animal):
    def nadar(self):
        print('Nadando')

class Halcon(Animal):
    def volar(self):
        print('Volando')

conejo = Conejo()
pez = Pez()
halcon = Halcon()

print(conejo.vivo)
conejo.comer()

halcon.volar()