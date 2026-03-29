#---Ejemplo 1----
def saludo():
    print('Hola')
    print('Que tengas un buen dia')

#saludo()

#---Ejemplo 2----
def saludo2(nombre):
    print('Hola ' + nombre)

#saludo2('Carlos')

#----Ejemplo 3---
def saludo3(nombre2):
    print('Hola', nombre2)

#nombre = input('Ingrese su nombre ')

#saludo3(nombre)

#----Ejemplo 4---
def saludo4(nombre, apellido, edad):
    print('Hola ' + nombre + ' ' + apellido)
    print('Tienes ' + str(edad) + ' Años')

nombre = input('Ingrese su nombre ')

saludo4(nombre, 'Apolinar', 40)