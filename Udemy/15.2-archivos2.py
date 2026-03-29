#MOSTRAR EL CONTENIDO DEL ARCHIVO EN LA TERMINAL

def app():
    #creando un archivo
    with open('archivo.txt') as archivo:
    # por defauld el 2 atributo es 'r' que significa lectura 
        for contenido in archivo:
            print(contenido.rstrip()) #rstrip() para remover los saltos en linea

app()