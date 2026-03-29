class Auto:

    #ejemplo de la variable de clases
    ruedas = 4

    #Variables de Instancias
    def __init__(self,marca,modelo,ano,color):        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color
    
    #Metodos dentro de la instancia
    def encendido(self):
        print('El auto esta encencido')

    def apagado(self):
        print('El auto esta apagado')