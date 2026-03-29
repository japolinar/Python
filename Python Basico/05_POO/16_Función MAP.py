tienda = [('Camisa', 20),
          ('Natalones', 25),
          ('Chaqueta', 50),
          ('Medias', 10)]

fun_euro = lambda datos : (datos[0], datos[1] * 0.96) #0.96 es el precio del euro de ese dia
fun_dolar = lambda datos : (datos[0], datos[1] / 0.96) #0.96 es el precio del euro de ese dia

tienda2 = list(map(fun_euro, tienda))

for i in tienda2:
    print(i)