class Coche:
    color = None

class Motocicleta:
    color = None

def cambiar_color(vehiculo, color):
    vehiculo.color = color

coche1 = Coche()
coche2 = Coche()
coche3 = Coche()
motocicleta = Motocicleta()

cambiar_color(coche1, 'Rojo')
cambiar_color(coche2, 'Azul')
cambiar_color(coche3, 'Verde')
cambiar_color(motocicleta, 'Negro')

print(coche1.color)
print(coche2.color)
print(coche3.color)
print(motocicleta.color)


