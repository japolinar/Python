#Ejemplo 1
estudiantes = ['Juan', 'Alex', 'Jorge', 'Lucy', 'Pedro']

estudiantes.sort()

for i in estudiantes:
    print(i)
print('--------')

#Ejemplo 2
estudiantes = ('Juan', 'Alex', 'Jorge', 'Lucy', 'Pedro') #cuando es una tupla por el ()

estudiantesList = sorted(estudiantes, reverse=True)

for i in estudiantesList:
    print(i)
print('--------')

#Ejemplo 3
estudiantes = [('Juan', 'F', 69),
               ('Alex', 'A', 24),
               ('Jorge', 'D', 33),
               ('Lucy', 'B', 19),
               ('Pedro', 'C', 43)] 

calificaciones = lambda tupla : tupla[1]
estudiantes.sort(key=calificaciones, reverse=True)

for i in estudiantes:
    print(i)
print('--------')

#Ejemplo 4
estudiantes = (('Juan', 'F', 69),
               ('Alex', 'A', 24),
               ('Jorge', 'D', 33),
               ('Lucy', 'B', 19),
               ('Pedro', 'C', 43)) #cuando es una tupla por el ()

calificaciones = lambda tupla : tupla[1]
estudiantesList= sorted(estudiantes, key=calificaciones, reverse=True)

for i in estudiantesList:
    print(i)