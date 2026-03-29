from tkinter import *

def enviar():
    input = texto.get('1.0', END)
    print(input)

root = Tk()
root.geometry('420x420')

texto = Text(root,
             bg='#ffffe0',
             font=('Ink Free', 25),
             height=8,
             width=20,
             padx=20,
             pady=20,
             fg='red')
texto.pack()

boton = Button(root, text='Enviar', command=enviar)
boton.pack(pady=5)

root.mainloop()