from multiprocessing import Process, cpu_count
import time

def contador(num):
    cont = 0
    while cont < num:
        cont += 1

def main():
    iniciar = time.perf_counter()
    a = Process(target=contador, args=(500000,))
    b = Process(target=contador, args=(500000,))

    a.start()
    b.start()

    a.join()
    b.join()

    fin = time.perf_counter()
    tiempo = fin - iniciar
    print('Finalizo en: ', tiempo, 'Segundos')

    print(cpu_count())  #<<-- para saber cuantos nucleos tiene ña cpu del PC

if __name__ == '__main__':
    main()



