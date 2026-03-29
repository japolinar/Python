try:
    with open('C:\\Users\\japol\\Desktop\\test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print('No se encontro el archivo', e)


