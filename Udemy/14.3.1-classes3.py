#Encapsulamiento

class  Restaurant:

    def __init__(self, nombre, categoria, precio): #con el __init__ se ejecuta automaticamente
        self.nombre = nombre #Atributos
        self.categotia = categoria #Atributos
        #self.precio = precio #Atributos por Defauld: Public, PROTECTED
        #self._precio = precio #Atributos PROTECTED
        self.__precio = precio #Atributos PRIVATE
 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categotia}, Precio: ${self.__precio} ')

#Instanciar la clase
restaurant = Restaurant('Pizzeria', 'Comida Italiana', 890)
restaurant.__precio = 300 #No sera posible mofificarlo con PRIVATE __
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas Full', 'Comida EEUU', 520)
restaurant2.__precio = 400 #No sera posible mofificarlo con PRIVATE __
restaurant2.mostrar_informacion()