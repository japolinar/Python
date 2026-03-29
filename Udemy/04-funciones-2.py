#FUNCIONES CON PARAMETROS Y ARGUMENTOS

def informacion(nombre, cargo = 'Desconocido'): #nombre, cargo son los parametros
    print(f'Soy {nombre}, soy {cargo}') #importante colocar la f antes de las comillas
    #La f sirve para formatear cadenas de forma más simple y legible

informacion('Desy', 'Informatico') #('') aca estan los argumentos
informacion('Kevin', 'Estudiante')
informacion('Zeus') #como no se le colocar el 2do argumento va aparecer 'Desconocido'
informacion('Jorge', 'Administrador')
