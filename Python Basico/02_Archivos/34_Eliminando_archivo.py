import os
#para eliminar carpetas que contienen archivos
import shutil

path = 'C:\\Users\\japol\\Desktop\\test.txt'
folder = 'C:\\Users\\japol\\Desktop\\prueba'

try:
    #para eliminar archivos
    os.remove(path)

    #para eliminar carpetas
    #os.rmdir(folder)

    #para eliminar carpetas que contienen archivos
    #shutil.rmtree(folder)

    print('Eliminado')
except FileNotFoundError as e:
    print('El archivo a eliminar no existe')
except PermissionError as e:
    print('No tienes permiso para elimar la carpeta')
except OSError as e:
    print('No puedes eliminar la carpeta con archivos dentro')
else:
    print(folder + ' Fue eliminado')

