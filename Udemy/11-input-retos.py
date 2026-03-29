calificacion = 0

pregunta_1 = input('Color del caballo de Bolivar \r\n').lower()

pregunta_2 = int(input('A partir de que edad es mayor de edad \r\n'))

pregunta_3 = input('Cual es el color del sol \r\n').lower()


if  pregunta_1 == 'blanco':
    calificacion += 1
    if pregunta_2 == 18:
        calificacion += 1
        if pregunta_3 == 'amarillo':
            calificacion += 1

print(f'Su nota fue de {calificacion}')
