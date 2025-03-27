import random as rnd

# Creacion de lista
n = int(input("N: "))
lista = []
for i in range(n):
    lista.append(rnd.randint(0, 100))
    
# Hallar maximo o minimo
max = lista[0]
posicion = 0

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]
        posicion = i

print(lista)
print(f"El numero maximo es: {max}, en la posicion {posicion}")

min = lista[0]
posmin = 0

for i, x in enumerate(lista):
    if x < min:
        min = x
        posmin = i
        
print(f"El numero minimo es: {min}, en la posicion {posmin}")

# Metodo de burbuja
for j in range(len(lista)):
    for i in range(len(lista)-1):
        if lista [i] > lista[i + 1]:
            # Estara es la manera de hacerlo si no estuviera en python
            """temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp"""
            # En python se puede resumir asi
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            
print(lista)