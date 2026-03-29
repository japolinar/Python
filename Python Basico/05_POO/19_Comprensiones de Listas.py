#Ejemplo 1
cuadrado=[]

for i in range(1,11):
    cuadrado.append(i*i)
print(cuadrado)

#Ejemplo 2
cuadrado2 = [i*i for i in range(1,11)]
print(cuadrado2)

#Ejemplo 3
estudiantes= [100,90,80,70,60,50,40,30,0]

estudiantes_aprobados= list(filter(lambda x: x >= 60, estudiantes))
print(estudiantes_aprobados)

#Ejemplo 4
estudiantes2= [100,90,80,70,60,50,40,30,0]

#estudiantes_aprobados2= [i for i in estudiantes2 if i >= 70]
estudiantes_aprobados2= [i if i >= 70 else '-' for i in estudiantes2 ]
print(estudiantes_aprobados2)