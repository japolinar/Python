import os

origen = 'C:\\Users\\japol\\Desktop\\test.txt'
destino = 'C:\\Users\\japol\\Desktop\\prueba\\copy.txt'

try:
    if os.path.exists(destino):
        print('Ya esxiste el archivo en el destino')
    else:
        os.replace(origen, destino)
        print(origen,' fue movido')
except FileNotFoundError as e:
    print(origen + ' No fue encontrado en archivo origen')

