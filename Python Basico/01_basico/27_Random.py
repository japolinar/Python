import random

x = random.randint(1, 6)
y = random.random()

lista = ['piedra', 'papel', 'tijera']
z = random.choice(lista)

cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
random.shuffle(cartas)

print(cartas)





