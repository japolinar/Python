#---Inicia el Juago-----
def new_game():
    respuestas = []
    respuestas_correstas = 0
    pregunta_num = 0

    for key in preguntas:
        print('-------------')
        print(key)
        for i in opciones[pregunta_num]:
            print(i)

        respuesta = input('Ingresa (A, B, C o D): ').upper()

        respuestas.append(respuesta)           

        respuestas_correstas += check_answer(preguntas.get(key), respuesta)
        
        pregunta_num += 1

    display_score(respuestas_correstas, respuestas, pregunta_num)

#---La funcion que valida respuestas_correstas-----
def check_answer(pregunta, respuesta):

    if pregunta == respuesta:
        print('-------------')
        print('CORRECTO!')
        return 1
    else:
        print('-------------')
        print('INCORRECTO!')
        return 0

#----La funcion que da el resultado----
def display_score(respuestas_correstas, respuestas, pregunta_num):
    print('*************')
    print('RESULTADO')
    print('-------------')

    print('Respuestas Correctas: ', end="")
    for i in preguntas:
        print(preguntas.get(i), end=" ")
    print()

    print('Tus Respuesta: ', end="")
    for i in respuestas:
        print(i, end=" ")
    print()

    #puntaje = int((respuestas_correstas/len(preguntas))*100)
    puntaje = int((respuestas_correstas/pregunta_num)*100)
    print('Puntaje: ' + str(puntaje) + '%')

#---La funcion que termina el juego o sigues jugando-----
def play_again():
    terminar = input('¿Quieres jugar de nuevo? (SI o NO): ').upper()

    if terminar == 'SI':
        return True
    else:
        return False


#---Variables-----
preguntas = {
    '¿Que idioma se habla en Brasil? ' : 'A',
    '¿Cual es el oseano mas grande del mundo? ' : 'B',
    '¿Cual es la estrella mas cercana a la tierra? ' : 'C',
    '¿Cual es el segundo pais mas grande del mundo? ' : 'A'
}
opciones = [
    ['A. Portugues', 'B. Español', 'C. Brasilero', 'D. Ingles'],
    ['A. Atlantico', 'B. Pacifico', 'C. Artico', 'D. Indico'],
    ['A. La luna', 'B. Alfa centauri', 'C. El sol', 'D. Ninguna'],
    ['A. Canada', 'B. Rusia', 'C. EE.UU', 'D. China'],
]

new_game()

while play_again():
    new_game()

print('-------------')
print('Gracias por participar!....')
