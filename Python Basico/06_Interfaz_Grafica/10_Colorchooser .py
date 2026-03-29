#Viene en el video 76: https://www.youtube.com/watch?v=Ne1iVY31LW0&list=PL5YuOOJ-FGGjAvcJcU5vMfVoc4S7sKvcm&index=76

from tkinter import *
from tkinter import colorchooser

def click():
    #color = colorchooser.askcolor()
    #colorHex = color[1]
    #root.configure(bg=colorHex)
    #print(colorHex)
    #Tambien se podria hacer todo en 1 solo linea
    root.configure(bg=colorchooser.askcolor()[1])

root = Tk()
root.geometry('480x480')
boton = Button(root, text='Has clik', command=click)

boton.pack(pady=20)


root.mainloop()
