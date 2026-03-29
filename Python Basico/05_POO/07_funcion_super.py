class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

class Cuadrando(Rectangulo):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho
        

class Cubo(Rectangulo):
    def __init__(self, alto, ancho, largo):
        self.largo = largo
        super().__init__(alto, ancho)

    def voluman(self):
        return self.alto * self.ancho * self.largo
        
cuadrado = Cuadrando(3, 3)
cubo = Cubo(3, 3, 3)

print(cuadrado.area())
print(cubo.voluman())
