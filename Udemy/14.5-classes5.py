#POLIMORFISMO

class  Restaurant:

    def __init__(self, nombre, categoria, precio): #con el __init__ se ejecuta automaticamente
        self.nombre = nombre #Atributos
        self.categotia = categoria #Atributos
        self.precio = precio #Atributos PRIVATE
 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categotia}, Precio: ${self.precio} ')

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

#Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    #Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categotia}, Precio: ${self.precio}, Alberca: {self.alberca} ')

    #Agregar un metodo que solo existe en hotal
    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
#mostrar la funcion  get_alberca
alberca = hotel.get_alberca()
print(alberca)