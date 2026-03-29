from tkinter import *
from tkinter import filedialog

def guardar():
    archivo = filedialog.asksaveasfile(initialdir='C:\\Users\\japol\\Desktop\\prueba',
                                       defaultextension='.txt',
                                       filetypes=[('Archivo de Texto', '*.txt'),
                                                  ('HTML', '.html'),
                                                  ('Todos los archivos', '.*')])
    if archivo is None:
        return

    archivoTxt = texto.get(1.0, END)
    archivo.write(archivoTxt)
    archivo.close()
    print(archivoTxt)

root = Tk()
root.geometry('200x200')

boton = Button(root, text='Guardar', command=guardar)
boton.pack(pady=20)

texto = Text(root)
texto.pack(padx=10, pady=5)

root.mainloop()