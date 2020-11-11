'''
Práctica 5. Ejercicio 3
Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.
Dame un número: 30
Dame otro número mayor que 30: 32
La suma desde 30 hasta a 32 es: 93
30+31+32 = 93

'''

print('''Te sumo números enteros en el rango que me des. Para ello escribe dos números 
(el segundo tiene que ser mayor en valor absoluto que el primero)
''')

numero_1 = int(input('Escribe el número de inicio '))
numero_2 = int(input('Escribe el número del final '))

suma = 0
for numero in range(numero_1, numero_2+1):
    suma += numero

print(f'La suma desde {numero_1} hasta {numero_2} es {suma}')
