from tkinter import *

def click():
    print('Has dado click')

root = Tk()

imagen = PhotoImage(file='C:\\Users\\japol\\Pictures\\Saved Pictures\\Python.png')

boton = Button(root, 
               text='Enviar',
               command=click,
               font=('Arial', 20, 'bold'),
               fg='white',
               bg='#613ec6',
               relief='groove',
               bd='10',
               activeforeground='white',
               activebackground='#452995',
               state='active',
               padx=10,
               pady=10,
               image=imagen,
               compound='top')

boton.pack(padx=50, pady=50)

root.mainloop()