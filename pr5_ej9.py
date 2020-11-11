'''
Práctica 5. Ejercicio 9
Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4
*****
*   *
*   *
*****

'''

print('Generador de bellos rectángulos huecos con asteriscos ******')

ancho = int(input('Indica el ancho del rectángulo '))
alto = int(input('Indica el alto del rectángulo '))

for elemento in range(1, alto+1):
    for elemento2 in range(1, ancho+1):
        if elemento == 1 or elemento == alto or elemento2 == 1 or elemento2 == ancho:
            print('*',  end=" ")
        else:
            print(' ', end=" ")
    print('\n')