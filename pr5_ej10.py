'''
Práctica 5. Ejercicio 10
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
    *
   ***
  *****
 *******
*********

'''

print('Triángulos centrados y asombrosos (III)')

altura = int(input('Indica la altura del triángulo '))
lista_anchura = range(0, 2*altura-1)

lista=  [[j for j in range(5)] for i in range(4)]
print(lista)

for i in range(0, altura):
    for j in lista_anchura:
        # Calculo la posición media de cada fila
        middleIndex = ((len(lista_anchura) - 1)/2)
        # Calculo los indices de empezar y finalizar los asteriscos
        startingIndex = int(middleIndex-i)
        lastIndex =  int(middleIndex +i)
        # miro si cada una de las posiciones cae dentro de la lista en la que tengo que poner asteriscos
        if j in lista_anchura[startingIndex:lastIndex+1]:
            print('*', end=" ")
        else:
            print(' ', end = " ")
    print('\n')


# for i in range(1, altura+1):
#     for j in range(altura - i):
#         print("  ", end="")
#     for j in range(1, 2*i): 
#         print("* ", end="")
#     print('\n')