"""

10.) Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor
entero dado por el usuario.

"""

number = int(input("Ingrese un valor entero maximo para la secuencia de finobacci = "))
    
n0, n1 = 0, 1

for i in range(number):

    print(n0, end=' ')

    fib = n0 + n1
    n0 = n1
    n1 = fib
    
print(n0)