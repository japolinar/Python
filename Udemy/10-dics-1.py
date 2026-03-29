#Los Diccionarios tambien llamados Objetos

#CREANDO UN DICCIONARIO SIMPLE
cancion = {
    'artista': 'Metalica', #llave y valor
    'cancion': 'Enter Sadman',
    'lanzamiento': 1992,
    'likes': 3000
}
print(cancion)

#acceder a los elementos por la llave
print(cancion['artista'])
print(cancion['lanzamiento'])

# Mezclar con string
artista = cancion['artista']
print(f'Estoy escuchando a: {artista}')

# Agregar valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# Reemplazar valores
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

# Eliminar valores
del cancion['lanzamiento']
print(cancion)
