"""

10.) Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor
entero dado por el usuario.

"""

number = int(input("Ingrese un valor entero maximo para la secuencia de finobacci = "))
    
n0, n1 = 0, 1

while True:
        
    fib = n0 + n1
    
    if n0 > number:
        print(f"El siguente numero de {number} en finobacci es: {n0}")
        break
    
    n0 = n1
    n1 = fib