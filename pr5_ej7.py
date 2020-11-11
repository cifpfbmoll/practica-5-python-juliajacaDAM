'''
Práctica 5. Ejercicio 7
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
****
***
**
*

'''

print('Triángulos asombrosos (II)')

altura = int(input('Indica la altura del triángulo '))

for i in reversed(range(altura+1)):
    print('*'*(i))