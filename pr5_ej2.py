'''
Práctica 5. Ejercicio 1
Escribe un programa que pida dos números y escriba qué números entre ese par de 
números son pares y cuáles impares

Ejemplo:
Escribe un número: 4
Escribe un número mayor que 4: 8
El número 4 es par
El número 5 es impar
El número 6 es par
El número 7 es impar
El número 8 es par

'''

print('Programa clasificador de números pares e impares')
numero_1 = int(input('Escribe el primer número a evaluar '))
numero_2 = int(input('Escribe el segundo número a evaluar '))
lista_numeros = [numero_1, numero_2]
# print(lista_numeros)

for numero in lista_numeros:
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')