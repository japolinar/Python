#diccionario = {key: expresion for (key, value) in iterable}

#Ejemplo 1
ciudades_en_F = {
    'New York': 32,
    'Boston': 75,
    'Los Angeles': 100,
    'Chicago': 50
}
ciudades_en_C = {key: round(((value - 32)*(5/9))) for (key, value) in ciudades_en_F.items() }
#print(ciudades_en_C)

#Ejemplo 2
clima = {
    'New York': 'Nieve',
    'Boston': 'Soleado',
    'Los Angeles': 'Soleado',
    'Chicago': 'Nublado'
}

clima_soleado = {key: value for (key, value) in clima.items() if value == 'Soleado'}
#print(clima_soleado)

#Ejemplo 3
climaM40 = {key: ('Calor' if value >= 40 else 'Frio' ) for (key, value) in ciudades_en_F.items()}
#print(climaM40)

#Ejemplo 4
def check_temp(value):
    if value >= 70:
        return 'Calor'
    elif 60 >= value >= 40:
        return 'Normal'
    else:
        return'Frio'

clima2 = {key: check_temp(value) for (key, value) in ciudades_en_F.items()}
print(clima2)