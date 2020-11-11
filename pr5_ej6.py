'''
Práctica 5. Ejercicio 6
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****'''

print('Triángulos asombrosos')

altura = int(input('Indica la altura del triángulo '))

for i in range(altura+1):
    print('*'*i)