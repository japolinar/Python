nombre_completo = "Maria Perez"
nombre = nombre_completo[0:5]
apellido = nombre_completo[6:11]
nombre_dos = nombre_completo[::2] 
nombre_invertido = nombre_completo[::-1]
url = 'https://www.google.com'
splice = slice(12, -4) 
sitio= url[splice]

#print(nombre)
#print(apellido)
#print('Su nombre es:', nombre + ' '+ apellido)
#print(nombre_dos)
#print(nombre_invertido)
#print(url[splice])
print(sitio)