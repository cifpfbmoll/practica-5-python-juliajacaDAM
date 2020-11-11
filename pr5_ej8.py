'''
Práctica 5. Ejercicio 8
Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
***
**
*
'''

print('Triángulos asombrosos (III)')

altura = int(input('Indica la altura del triángulo '))

for i in range(altura):
    print('*'*i)

for i in reversed(range(altura+1)):
    print('*'*i)