nombre = 'Jorge Apolinar'

# if nombre[0].islower() : 
#     nombre = nombre.capitalize()    
# print(nombre)

primer_nombre = nombre[:5].upper()
apellido = nombre[6:].lower()
ultimo_caracter = nombre[-1]

print(primer_nombre, apellido)
print(ultimo_caracter)