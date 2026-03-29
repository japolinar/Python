import random

lista = ['roca', 'papel', 'tijera']

while True:
    computadora = random.choice(lista)
    jugador = ''

    while jugador not in lista:
        jugador = input('roca, papel, tijera? ').lower()

    if jugador == computadora:
        print('Computadora:', computadora)
        print('Jugador:', jugador)
        print('Empate!')
    elif jugador == 'roca':
        if computadora == 'papel':
            print('Computadora:', computadora)
            print('Jugador:', jugador)
            print('Perdiste!')
        if computadora == 'tijera':
            print('Computadora:', computadora)
            print('Jugador:', jugador)
            print('Ganaste!')
    elif jugador == 'papel':
        if computadora == 'tijera':
            print('Computadora:', computadora)
            print('Jugador:', jugador)
            print('Perdiste!')
        if computadora == 'roca':
            print('Computadora:', computadora)
            print('Jugador:', jugador)
            print('Ganaste!')
    elif jugador == 'tijera':
        if computadora == 'roca':
            print('Computadora:', computadora)
            print('Jugador:', jugador)
            print('Perdiste!')
        if computadora == 'papel':
            print('Computadora:', computadora)
            print('Jugador:', jugador)
            print('Ganaste!')
            
    jugar_de_nuevo = input('Quiere seguir jugando?, (si, no) ').lower()

    if jugar_de_nuevo != 'si':
        break
print('Gracias por jugar!...')

