#Ejemplo con elif

ocupacion = 'Estudiante'

if ocupacion == 'Estudiante':
    print(f'Tienes 50% de descuento')
elif ocupacion == 'Jubilado':
    print(f'Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print(f'Tienes 10% de descuento')
else:
    print('Debes pagar el 100%')
