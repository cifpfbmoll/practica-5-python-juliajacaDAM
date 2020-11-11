'''
Práctica 5. Ejercicio 11
Escribe un programa que pida un número e imprima todos sus divisores.
Dame un número: 200
Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200

'''

print('calculadora de divisores!')
numero = int(input('Introduce un número entero para calcular sus divisores'))

lista_divisores = []
for divisor in range(1, numero+1):
    if numero % divisor == 0:
        lista_divisores.append(divisor)

print(f'Los divisores de {numero} son {lista_divisores}')
