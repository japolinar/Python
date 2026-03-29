nombre_usuario = ['Alex', 'Smith', 'Hermano'] #<<-- [Lista]
contrasena = ('123', 'abc', 'contra') #<<--(Dupla)
fecha_inicio_seccion = ['01/04/2023', '05/08/2024', '21/05/2021']

usuarios = list(zip(nombre_usuario, contrasena, fecha_inicio_seccion))
usuarios2 = dict(zip(nombre_usuario, contrasena))

#print(usuarios)

for k, v, i in usuarios:
    print(k + ': ' + v +': ' + i)

for key, value in usuarios2.items() :      
    print(key + ': ' + value)
