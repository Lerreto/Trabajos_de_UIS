"""

2.) Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el
número primo de valor más cercano, en este caso menor o igual, al número leído

"""

while True:
    n = int(input("Ingrese un numero entero: "))

    if n > 2:
        break
    else:
        print("\nTiene que ser mayor de 2\n")

for i in range(n, 0, -1):
    contador = 0
    for x in range(1, n+1):
        if i % x == 0:
            contador +=1
    
    if contador == 2:
        numero_primo = i
        break
    

print(f"El mayor numero primo mas cercano es: {numero_primo}")