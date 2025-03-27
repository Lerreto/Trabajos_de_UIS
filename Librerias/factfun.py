def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return(fact)

m = 20
resultado = factorial(m)
print(f"El resultado = {resultado}")
print(f"Factorial de {10} es {factorial(10)}")