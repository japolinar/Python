from tkinter import *

comida = ['Pizze', 'Hamburguesa', 'Hotdog']

root = Tk()

x = IntVar()

def order():
    if(x.get() == 0):
        print('Has ordenado una Pizza')
    elif(x.get() == 1):
        print('Has ordenado una Hamburguesa')
    elif(x.get() == 2):
        print('Has ordenado una Hotdog')
    else:
        print('No has ordenado')


for index in range(len(comida)):
    radioButton = Radiobutton(root, 
                              text=comida[index],
                              variable=x,
                              value=index,
                              padx=20,
                              font=('Arial', 20),
                              indicatoron=0,
                              width=10,
                              command=order,
                              bg='#1a5276'
                              )
    radioButton.pack(padx=15, pady=15, anchor=W)


root.mainloop()