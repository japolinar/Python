from tkinter import *

def mostrar():
    if(x.get() ==1):
        print('Estas de acuerdo')
    else:
        print('No estas de acuerdo')

root = Tk()

x = IntVar()

imagen = PhotoImage(file='C:\\Users\\japol\\Pictures\\Saved Pictures\\Python.png')

check_button = Checkbutton(root,
                           text='Acepto',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=mostrar,
                           font=('Arial', 20),
                           fg='red',
                           bg='#000',
                           padx=10,
                           pady=10,
                           activeforeground='red',
                           activebackground='#000',
                           image=imagen, 
                           compound='left')

check_button.pack(padx=50, pady=50)

root.mainloop()
