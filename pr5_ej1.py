'''
Práctica 5. Ejercicio 1
Escribe un programa que escriba a los siguientes número (la separación entre número
es para facilitar cuántos números se deben escribir en cada bucle) y en el que la 
función range que utilices tenga un ÚNICO argumento y que el valor de este se corresponda
con el número de elementos que aparecen en la lista ( por Ejemplo, para la primera lista range (10)).

'''
print('Lista 1')
for i in range(10):
    print(i+1, end= " ")

print('\nLista 2')
for i in range(10):
    print((i+1)*2, end= " ")

    
print('\nLista 3')
for i in range(10):
    print((i*2)+20, end= " ")

print('\nLista 4')
for i in range(6):
	print((i*4)+10, end= " ")

print('\nLista 5')
for i in range(9):
	print(i*-5 + 40, end= " ")