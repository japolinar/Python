playlist = {} # Diccionario vacio
playlist['canciones'] = [] # Lista vacia de canciones

# Funcion principal
def app():    
    #Agregar playpl 
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar tu playlist? \r\n')        
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist.upper()
            # Ya tenemos un nombre, desactivar el true
            agregar_playlist = False
            # Mandar llamar la funcion para agregar canciones
            agregar_canciones()
            #print(playlist)

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #Preguntar al usuario que cancion desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\n Agrega canciones para la playlist {nombre_playlist} \r\n'
        pregunta += 'Escribe "x" para dejar de escribir canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'x':
            #Dejar de agregar canciones 
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrando_resumen()
        else:
            #agregar las canciones
            playlist['canciones'].append(cancion.upper())

def mostrando_resumen():
    nombre_playlist = playlist['nombre']    
    print(f'\r\nPlaylist: {nombre_playlist} \r\n')
    print('Cancion:\r')
    for cancion  in playlist['canciones']:
        print(f'.- {cancion}')

# Llamar la app principal
app()
