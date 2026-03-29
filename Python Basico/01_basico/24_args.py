def sumar(*args):
    suma = 0
    cosas = list(args)
    cosas[2] = 0

    for i in cosas:
        suma += i
    return suma

print(sumar(3, 5, 8, 7, 1))