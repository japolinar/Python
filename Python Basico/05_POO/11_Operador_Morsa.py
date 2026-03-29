#Ejemplo 1
#print(feliz = True) #de esta forma da error
#print(feliz := True) #colocar los 2 punto hace asignar un valor a la variable

#Ejemplo 2
# comidas = []
# while True:
#     comida = input('¿Que comida te gusta? ').lower()
#     if comida == 'salir':
#         break
#     comidas.append(comida)
# print(comidas)

#Ejemplo 3
comidas = []

while (comida := input('¿Que comida te gusta? ').lower()) != 'salir':
    comidas.append(comida)

print(comidas)
