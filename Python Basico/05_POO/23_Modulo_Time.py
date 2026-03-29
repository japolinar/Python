import time

# print(time.ctime(0))
# print(time.time())
# print(time.ctime(time.time()))

tiempo_actual = time.localtime()
#print(time.localtime())
tiempo =  time.strftime('%d-%m-%Y %H:%M:%S', tiempo_actual)

print(tiempo)

#time asctime
tiempo_tupla = (2023, 4, 14, 4, 20, 0, 0, 0, 0)
cadena_tiempo = time.asctime(tiempo_tupla)
print(cadena_tiempo)