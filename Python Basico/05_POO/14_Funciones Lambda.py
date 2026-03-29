#Ejemplo 1
def doble(x):
    return x * 2

print(doble(5))

#Ejemplo 2
doble2 = lambda x: x * 2

print(doble2(10))

#Ejemplo 3
multiplicar = lambda x, y: x * y
suma = lambda x,y,z: x + y + z

print(multiplicar(5, 7))
print(suma(5,4,2))

#Ejemplo 4
nombre_completo = lambda nombre, apellido: nombre + " " + apellido

print(nombre_completo('Kein', 'Apol'))

#Ejemplo 5
check_edad = lambda edad: True if edad >= 18 else False

print(check_edad(17))