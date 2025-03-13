"""

4.) Construir un programa que lea dos números y si son ambos pares o ambos impares, halle el máximo
común divisor de dos números; si uno es par y el otro impar, el programa debe hallar el mínimo común
múltiplo.

"""

n1 = int(input("Ingrese el primer numero = "))
n2 = int(input("Ingrese el segundo numero = "))

mcd = 1

nmax = max(n1, n2)
for x in range(nmax + 1, 1, -1):
    if (n1 % x) == 0 and (n2 % x == 0):
        mcd = x
        break

if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0):
    print(f"El MCD de {n1} y {n2} es = {mcd}")
else:
    mcm = n1 * n2 / mcd
    print(f"El MCM de {n1} y {n2} es = {mcm}")





