#List = Lista ->> Arrays o Arreglo

lenguaje = ['Python', 'Javascript', 'PHP', 'C#']

print(lenguaje)
#Los list comienda en la posision 0
print(lenguaje[0])
print(lenguaje[3])

#Los Ordena alfabeticamente
lenguaje.sort()
print(lenguaje )

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguaje[3]}'
print(aprendiendo)

#Modificando valores de una lista o arreglos
lenguaje[2] = 'Kotlin'
print(lenguaje)

#Agregar elemento a una lista o arreglos
lenguaje.append('Ruby')
print(lenguaje)

#Eliminar elemento a una lista o arreglos
del lenguaje[1]
print(lenguaje)

#De otra forma para eliminar
lenguaje.pop() #elimina el ultimo elemento
print(lenguaje)

#Eliminar con pop una osicion en especifico
lenguaje.pop(0)
print(lenguaje)

#Eliinar por nombre
lenguaje.remove('Kotlin')
print(lenguaje)



