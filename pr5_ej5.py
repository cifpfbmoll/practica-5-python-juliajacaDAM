'''
Práctica 5. Ejercicio 5
Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 3
*****
*****
*****

'''
print('Generador de bellos rectángulos con asteriscos ******')

ancho = int(input('Indica el ancho del rectángulo '))
alto = int(input('Indica el alto del rectángulo '))

# lista = [['*' for elemento in range(alto+1)] for elemento in range(ancho+1)]
# print(lista)

for elemento in range(0, alto):
    for elemento2 in range(0, ancho):
        print('*',  end=" ")
    print('\n')