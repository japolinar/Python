import os

ruta= 'C:\\Users\\japol\\Desktop\\test.txt'

if os.path.exists(ruta):
    print('El archivo existe')
    if os.path.isfile(ruta):
        print('Es un archivo')
    elif os.path.isdir(ruta):
        print('Es un directorio')
else:
    print('El archivo No existe')         

# La librería os de Python permite realizar operaciones con el sistema operativo, 
# como crear carpetas, renombrar archivos, leer y escribir archivos, entre otras. 

# Funciones del módulo os 
# Crear un directorio: os.mkdir("my_directory")
# Verificar si existe un archivo: os.path.exists("file.txt")
# Listar el contenido de un directorio: os.listdir("my_directory")
# Cambiar el directorio de trabajo actual: os.chdir("new_directory")
# Cambiar el nombre de un archivo: os.rename("old_file.txt", "new_file.txt")
# Acceder a variables de entorno: os.environ["HOME"]
# Obtener el nombre del usuario que inició sesión en el terminal: os.getuser()
