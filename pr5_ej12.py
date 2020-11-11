'''
Práctica 5. Ejercicio 12
Escribe un programa que pida un número y escriba si primo o no
Dame un número: 123
El número 123 no es primo
Dame un número:127
El número 127 es primo

'''

print('Averigua si tu número favorito es primo o no')
numero= int(input('Escribe aquí el número '))

primo = True
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False

print(f'El número {numero} es primo') if primo else print(f'El número {numero} no es primo')