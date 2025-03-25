angulo, n, suma = float(input("Ingrese el angulo: ")), int(input("Ingrese n: ")), 0
angulo = (angulo * 3.14159) / 180
print(angulo)

for x in range(n + 1):
    fact = 1
    kmax = 2 * x + 1
    for k in range(1, kmax + 1):
        fact *= k
    suma += (((-1)**x) * (angulo**(2*x + 1))) / fact

print(suma)