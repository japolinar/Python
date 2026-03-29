from tkinter import *

def submit():
    print('La temperatura es: ' + str(scala.get()) + '° grados' )

root = Tk()

scala = Scale(root,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,
              font=('Arial', 15),
              tickinterval=10,
              resolution=2,
              troughcolor='#ff6601',
              fg='red',
              bg='#000')

scala.set(30)
scala.pack(padx=15, pady=15)

boton = Button(root,
               text='Enviar',
               command=submit)

boton.pack(pady=10)

root.mainloop()