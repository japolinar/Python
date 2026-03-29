#Clases

class  Restaurant:
    def agregar_restaurant(self, nombre):
        #print('Agregando....')
        #importante colocar el argumento (self)
        self.nombre = nombre #esto se conoce como atributo de la clase

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesas Full')
restaurant2.mostrar_informacion()

#Otra forma de mostrar los datos
print('-------------')
print(f'Nombre Restaurant: {restaurant.nombre} ')
print(f'Nombre Restaurant: {restaurant2.nombre} ')