from tkinter import *

# --Funciones--S
def abrirArchivo():
    print('Abrir Archivo')

def guardarArchivo():
    print('Guardar Archivo')

def cortarArchivo():
    print('Cortar Archivo')

def copiarArchivo():
    print('Copiar Archivo')

def pegarArchivo():
    print('Pegar Archivo')

root = Tk()

guardarImagen = PhotoImage(file='C:\\Users\\japol\\Pictures\\Saved Pictures\\boton-guardar (1).png')
abrirImagen = PhotoImage(file='C:\\Users\\japol\\Pictures\\Saved Pictures\\carpeta-abierta (1).png')
cerrarImagen = PhotoImage(file='C:\\Users\\japol\\Pictures\\Saved Pictures\\cerrar-sesion (1).png')

menuBar = Menu(root)
root.configure(menu=menuBar)

#--Menu--
fileMenu = Menu(menuBar, tearoff=0, font=('MV Boli',15))
menuBar.add_cascade(label='Archivo', menu=fileMenu)
fileMenu.add_command(label='Abrir', command=abrirArchivo, image=abrirImagen, compound='left')
fileMenu.add_command(label='Guardar', command=guardarArchivo, image=guardarImagen, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Salir', command=quit, image=cerrarImagen, compound='left')

#--Menu--
editMenu = Menu(menuBar, tearoff=0, font=('MV Boli',15))
menuBar.add_cascade(label='Editar', menu=editMenu)
editMenu.add_command(label='Cortar', command=cortarArchivo)
editMenu.add_command(label='Copiar', command=copiarArchivo)
editMenu.add_command(label='Pegar', command=pegarArchivo)
editMenu.add_separator()
editMenu.add_command(label='Salir', command=quit)

root.mainloop()