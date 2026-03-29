#Ejemplo 1
def habraAlto(texto):
    return texto.upper()

def habraBajo(texto):
    return texto.lower()

def hola (fun):
    texto = fun('hola') 
    print(texto)

hola(habraAlto)
hola(habraBajo)

#Ejemplo 2
def divisor(x):
    def dividendo(y):
        return y / x
    return dividendo

divide = divisor(2)
print(divide(10))

