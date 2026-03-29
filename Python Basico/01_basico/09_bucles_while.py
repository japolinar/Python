# nombre= ""

# while not nombre or len(nombre) == 0 : 
#     nombre = input('¿Cual es tu nombre? ')

# print('Hola', nombre)


#--otro ejemplo con edad
nombre= ""
edad= 0
while not nombre or len(nombre) == 0 or not edad or edad == 0 :
    nombre= input('¿Escribe tu nombre? ')
    edad= int(input('¿Cual es tu edad? '))

print('Tu nombre es: '+ nombre)
print('Tienes ' + str(edad) + ' años')

