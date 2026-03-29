#HERENCIA

class  Restaurant:

    def __init__(self, nombre, categoria, precio): #con el __init__ se ejecuta automaticamente
        self.nombre = nombre #Atributos
        self.categotia = categoria #Atributos
        self.__precio = precio #Atributos PRIVATE
 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categotia}, Precio: ${self.__precio} ')

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

#Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()
