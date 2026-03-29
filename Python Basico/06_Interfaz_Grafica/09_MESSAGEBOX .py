from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='Hola', message='Jorge Apolinar')
    #messagebox.showerror(title='Hola', message='Jorge Apolinar')
    #messagebox.showwarning(title='Hola', message='Jorge Apolinar')
    #messagebox.askokcancel(title='Hola', message='Jorge Apolinar')
    #messagebox.askretrycancel(title='Hola', message='Jorge Apolinar')
    #messagebox.askquestion(title='Hola', message='Jorge Apolinar')
    #messagebox.askyesnocancel(title='Hola', message='Jorge Apolinar', icon='warning')
    if(messagebox.askyesno(title='Hola', message='Jorge Apolinar')):
        print('Presionaste Si')
    else:
        print('Presionaste No')

root = Tk()

button = Button(root, text='Click', command=click)
button.pack(padx=60, pady=30)


root.mainloop()


