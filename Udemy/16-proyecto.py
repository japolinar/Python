import os

CARPETA = 'Udemy/contacto/' #Carpeta de contacto
EXTENSION = '.txt' # Extencion de archivos
#En mayuscula porque es una constante, no debe modificar el valor

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe
    crear_directorio()

    #Muestra el menu de opciones
    mostrar_menu()

    #Preguntar al usuario la accion a relaizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion:\r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            print('\n------------------')
            print('Saliste de la app')
            print('------------------\n')
            preguntar = False
        else:
            print('\n------------------')
            print('Opcion no valida!!!')    
            print('------------------\n')

def crear_directorio():
    if not os.path.exists(CARPETA): #pregunta si existte la carpeta
        #crear carpeta
        os.makedirs(CARPETA)
    #else:
        #print('La carpeta ya existe!!!')

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')
    print('6) Salir')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

def agregar_contacto():
    print('\n------------------')
    print('Agregue el contacto')
    print('-------------------')
    nombre_contacto = input('Nombre del contacto:\r\n')

    #Revisar si el nombre del contacto existe
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: # w es escritura

            #Resto de los campos
            telefono_contacto = input('Agrega el telefono:\r\n')
            categoria_contacto = input('Agrega la categoria:\r\n')

            #Instanciamos la clase, pasandoles los agumentos
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r')
            archivo.write('Telefono: ' + contacto.telefono + '\r')
            archivo.write('Categoria: ' + contacto.categoria + '\r')

            #Mostrar un mensaje de exito
            print('\r\nContacto creado con exito!!!\r\n')

    else:
        print('\nEl contacto ya existe!!!\n')

    #Reiniciar la app
    app()

def editar_contacto():
    print('\n----------------------------')
    print('Escribe el contacto a editar')
    print('----------------------------')
    nombre_anterior = input('\nNombre del contacto a editar:\r\n')

    #Revisar si el nombre del contacto existe
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo: # w es escritura
            
            #Resto de los campos
            nombre_contacto = input('Agrega el nuevo Nombre del contacto:\r\n')
            telefono_contacto = input('Agrega el nuevo telefono:\r\n')
            categoria_contacto = input('Agrega la nueva categoria:\r\n')

            #Instanciamos la clase, pasandoles los agumentos
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r')
            archivo.write('Telefono: ' + contacto.telefono + '\r')
            archivo.write('Categoria: ' + contacto.categoria + '\r')

        #Renombrar el archivo ojo debe estar fuera del with para evitar el error PermissionError
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        #Mostrar un mensaje de exito
        print('\r\nContacto Editado con exito!!!\r\n')

    else:
        print('\n---------------------')
        print('No existe el contacto')
        print('---------------------')
    
    #Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contactos:
            print('\n------------------')
            for linea in contactos:
                #Imprime Los contenidos
                print(linea.rstrip())
            #Imprime el separados
            print('------------------')

    #Reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar:\r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\nInformacion de contacto:')

            print('\n------------------')
            for linea in contacto:
                #Imprime Los contenidos
                print(linea.rstrip())
            #Imprime el separados
            print('--------------------')
            
    except IOError:
        print('\n---------------------')
        print('El Contacto No Existe')
        print('---------------------')
        #print(IOError)

    #Reiniciar la app
    app()

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar:\r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\n---------------------')
        print('El contacto ' + nombre + ' ha sido eliminado!!!!')
        print('---------------------')
    except IOError:
        print('\n---------------------')
        print('No existe el contacto')
        print('---------------------')
        #print(IOError)

    #Reiniciar la app
    app()

app()