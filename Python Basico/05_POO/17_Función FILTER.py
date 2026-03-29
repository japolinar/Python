amigos = [('Juan', 22),
          ('Alex', 19),
          ('Jorge', 25),
          ('Lucy', 17),
          ('Pedro',  20),
          ('Sofia',  16)]#cuando es una tupla por el ()

edad = lambda datos: datos[1] >= 18

amigosMayor18= list(filter(edad, amigos))

for i in amigosMayor18:
    print(i)

