from tkinter import *

def enviar():
    nombre_usuario = imput.get()
    print('Hola ' + nombre_usuario)
    imput.delete(0, END)

def reset():
    imput.delete(0, END)

def eliminar():
    imput.delete( len(imput.get()) - 1, END )

root = Tk()

imput = Entry(root,
              font=('Arial', 50),
              fg='white',
              bg='black'
              )
imput.pack(padx=40, pady=40, side=LEFT) 

boton_enviar = Button(root, text='Enviar', command=enviar, bg='green', fg='white', cursor='hand2')
boton_enviar.pack(padx=20, side=LEFT)

boton_reset = Button(root, text='Resetear', command=reset, bg='red', fg='white', cursor='hand2')
boton_reset.pack(padx=20, side=LEFT)

boton_eliminar = Button(root, text='Eliminar', command=eliminar, bg='blue', fg='white', cursor='hand2')
boton_eliminar.pack(padx=20, side=RIGHT)

root.mainloop()