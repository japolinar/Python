from tkinter import *

root = Tk()
#root.geometry('500x400')
root.title('Programa de Python')

label = Label(root, 
              text='Hola Mundo, para programar con Python', 
              font=('Arial', 40, 'bold'), 
              fg='white', 
              background='black',
              relief='raised',
              bd=10,
              padx=50,
              pady=40)
label.pack(padx=150, pady=150)
##label.place(x=100, y=100)

root.mainloop()