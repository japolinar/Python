# nombre = input('Cual es tu nombre: \r\n') # \r\n <<-- es para crear un salto de linea
# print(f'Hola {nombre}')

#LEER DATOS QUE SERAN NUMEROS
# edad = input('¿Cual es tu edad? \r\n')
# #convertir edad (string)(str) a int
# edad = int(edad)
# if edad >= 18:
#     print('Ya puedes votar')
# else:
#     print('Aun no puedes votar')

#Mezclar con operadores
numero = input('Agrega un numero y te dire si es par o impar \r\n')
numero = int(numero)

# % 2 == 0 <<-- se conoce como el modulo y su valor es 0
if numero % 2 == 0 :
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')

