from tkinter import *
from tkinter import filedialog

def abrir():
    ruta = filedialog.askopenfilename(initialdir='C:\\Users\\japol\\Desktop\\prueba', 
                                      title='Abrir Archivo',
                                      filetypes=(('Archivo de Texto', '*.txt'), ('Todos los archivo', '*.*')))
    #ruta = filedialog.askopenfilename()
    archivo = open(ruta, 'r')
    print(archivo.read())
    archivo.close()

root = Tk()
root.geometry('300x300')
boton= Button(root, text='Abrir', command=abrir)
boton.pack(pady=20)

root.mainloop()