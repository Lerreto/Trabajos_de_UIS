"""

8.) Escribir un programa que lea un entero positivo y escriba el mismo número conformado por las cifras
del número leído más 1. Si al sumar uno a una cifra da 10 se debe poner 0. Por ejemplo:
12345 → 23456.
987654 → 098765.

"""

n = input("Ingrese un entero positivo: ")
m = ""

for i in n:
    i = int(i) + 1
    if i == 10:
        i = 0
    m += str(i)

print(f"{n} ---> {m}")