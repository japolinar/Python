from automovil import Auto 

auto_1 = Auto('Chevy', 'Corvette', 2023, 'azul')
auto_2 = Auto('Ford', 'Mustang', 2022, 'rojo')

print(auto_1.marca)
print(auto_1.modelo)
print(auto_1.ano)
print(auto_1.color)

auto_1.ruedas = 2

#print('Tienes ' + str(Auto.ruedas) + ' ruedas')
print(auto_1.ruedas)
print(auto_2.ruedas)

auto_1.encendido()

