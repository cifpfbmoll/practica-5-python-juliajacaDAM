'''
Práctica 5. Ejercicio 4
Escribe un programa que pida un número y calcule su factorial.
Dame un número: 5
El factorial de 5 es: 120
'''

numero = int(input('Escribe un número entero para calcular su factorial '))

factorial= 1
for factor in range(1, numero+1):
    factorial *= factor


print(f'El factorial de {numero} es {factorial}')
