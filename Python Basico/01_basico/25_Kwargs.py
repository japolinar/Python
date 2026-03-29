def hola(**kwargs):
    print('Hola', end=' ')
    for clave, valor in kwargs.items():
        print(valor, end=' ')

hola(titulo= 'Sr.', nombre='Jorge', apellido='Apolinar', lenguage='Python')