#reduce(funcion, interable)
import functools

#Ejemplo 1
letras= ['h', 'o', 'l', 'a']

palabra = functools.reduce(lambda x,y : x + y, letras).upper()
print(palabra)

#Ejemplo 2
factorial = [5,4,3,2,1]

resultado= functools.reduce(lambda x,y :  x * y, factorial)
print(resultado)

