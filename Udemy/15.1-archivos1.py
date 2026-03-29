#CREANDO Y ESCRIBIENDO DATOS EN ARCHIVOS

def app():
    #creando un archivo
    archivo = open('Udemy/archivo.txt', 'w') # w es escritura, si no existe lo creara 

    #Generar numero en archivo
    for i in range(1, 16):
        archivo.write('Esta es la linea: ' + str(i) +'\r' )

    print('\n-------------------------------')
    print('Archivo Creado correctamente!!!')
    print('-------------------------------')

    #Cerrando el archivo
    archivo.close()

app()