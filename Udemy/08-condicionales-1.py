#Revisar si una condicion es mayor a
balance = 0

if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

#Likes
likes = 200

if likes >= 200:
    print(f'Excelene, {likes} likes')
else:
    print('falta poco')

# if con texto
lenguaje = 'Python'

if not lenguaje == 'Python':
    print('Excelente')

# Evaluar con boolean
usuario = True

if not usuario:
    print('Autenticado')
else:
    print('Debes iniciar seccion')

#Evaluar los elemento de una list
lenguajes = ['Python', 'Javascript', 'PHP', 'C#', 'GO', 'Kotlin', 'Ruby']

if 'PHP' in lenguajes:
    print('Si esta en la lista')
else:
    print('No esta en la lista')

# If Anidados
usuario2 = True
usuario_adm = True
if usuario2:
    if usuario_adm:
        print('Aceeso total')
    else:
        print('Autenticado')
else:
    print('Debes iniciar seccion')

