"""

9.) Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a
un valor entero dado por el usuario.

"""

number = int(input("Ingrese un valor entero maximo para la secuencia de finobacci = "))
    
n0, n1 = 0, 1

while True:

    print(n0, end=' ')
    fib = n0 + n1
    n0 = n1
    n1 = fib
    
    if n0 > number:
        break