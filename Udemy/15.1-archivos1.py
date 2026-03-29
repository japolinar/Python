#CREANDO Y ESCRIBIENDO DATOS EN ARCHIVOS

def app():
    #creando un archivo
    archivo = open('archivo.txt', 'w') # w es escritura, si no existe lo creara 

    #Generar numero en archivo
    for i in range(1, 11):
        archivo.write('Esta es la linea: ' + str(i) +'\r' )

    #Cerrando el archivo
    archivo.close()

app()