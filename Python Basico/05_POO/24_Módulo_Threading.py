import threading
import time

# print(threading.active_count())
# print(threading.enumerate())

def desayunar():
    print('Iniciando..desayunar..')
    time.sleep(3)
    print('Finalizando....')

def tomar_cafe():
    print('Iniciando..tomar_cafe..')
    time.sleep(4)
    print('Finalizando....')

def estudiar():
    print('Iniciando..estudiar..')
    time.sleep(5)
    print('Finalizando....')

inicio = time.perf_counter()

# desayunar()
# tomar_cafe()
# estudiar()
x = threading.Thread(target=desayunar, args=())
x.start()

y = threading.Thread(target=tomar_cafe, args=())
y.start()

z = threading.Thread(target=estudiar, args=())
z.start()

x.join()
y.join()
z.join()

fin = time.perf_counter()
tiempo = fin - inicio
print(tiempo)