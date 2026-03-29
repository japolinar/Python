#Operadores and y or

usuario_logueado = True
usuario_Admin = False

if usuario_logueado and usuario_Admin:
    print('Administrador')
elif usuario_logueado:
    print('Usuario Logueado')
else:
    print('Debes de iniciar seccion')

