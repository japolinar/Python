from tkinter import *

windows = Tk()
windows.geometry('500x400')
windows.title('Programa de Python') #<<--Cambiar el titulo

icono = PhotoImage(file='C:\\Users\\japol\\Pictures\\Saved Pictures\\Python.png')
windows.iconphoto(True, icono) #<<--incorporar un logo

windows.config(background='black') #<<--cambiar el fondo de la ventana

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

center_window(windows) #<<-- centrar la ventana

windows.mainloop()