class Pato:
    def caminar(self):
        print('Este pato esta caminando')

    def hablar(self):
        print('Este pato esta haciendo cuac')

class Gallina:
    def caminar(self):
        print('Esta gallina esta caminando')

    def hablar(self):
        print('Esta gallina esta cacareando')

class Persona:
    def atrapar(self, animal):
        animal.caminar()
        animal.hablar()

        print('lo atrapaste!!')

pato = Pato()
gallina = Gallina()
persona = Persona()

persona.atrapar(pato)

