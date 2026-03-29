#Abstracción y Constructores

class  Restaurant:

    def __init__(self, nombre, categoria, precio): #con el __init__ se ejecuta automaticamente
        self.nombre = nombre #Atributos
        self.categotia = categoria #Atributos
        self.precio = precio #Atributos
 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categotia}, Precio: ${self.precio} ')

#Instanciar la clase
restaurant = Restaurant('Pizzeria', 'Comida Italiana', 890)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas Full', 'Comida EEUU', 520)
restaurant2.mostrar_informacion()


