class Presa:
    def huir(self):
        print('El animal huye')

class Depredadr:
    def cazar(self):
        print('El animal esta cazando')

class Conejo(Presa):
    pass

class Halcon(Depredadr):
    pass

class Pez(Presa, Depredadr):
    pass

conejo = Conejo()
halcon = Halcon()
pez = Pez()


conejo.huir()
halcon.cazar()
pez.huir()
pez.cazar()
