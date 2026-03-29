try:
    numerador = int(input('Ingrese un numero: '))
    denominador = int(input('Ingrese un numero: '))
    resultado = numerador/denominador    
except ZeroDivisionError as e:
    print(e)
    print('No puedes divir por 0')
except ValueError as e:
    print(e)
    print('No puedes colocar letras, solo numeros')
except Exception as e:
    print(e)
    print('Algo salio mal')
else:
    print(resultado)
finally:
    print('Siempre se ejecuta al final')


