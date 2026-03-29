from tkinter import *

def submt():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print('Su orden es: ')
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #print(listbox.get(listbox.curselection()) + ' - Eliminado')
    #listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        print(listbox.get(index) + ' - Eliminado')        
        listbox.delete(index)

    listbox.config(height=listbox.size())    
   
root = Tk()
listbox = Listbox(root,
                  bg='#f7ffde',
                  font=('Arial', 35),
                  width=15,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'Pizza 1')
listbox.insert(2, 'Pizza 2')
listbox.insert(3, 'Pizza 3')
listbox.insert(4, 'Pizza 4')
listbox.insert(5, 'Pizza 5')

listbox.config(height=listbox.size())

entryBox = Entry(root)
entryBox.pack()

submitButton = Button(root,
                      text='Enviar',
                      command=submt)
submitButton.pack()

addButton = Button(root,
                      text='Agregar',
                      command=add)
addButton.pack()

deleteButton = Button(root,
                      text='Eliminar',
                      command=delete)
deleteButton.pack()

root.mainloop()


