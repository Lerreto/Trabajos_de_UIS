from os import O_TRUNC
import random as rnd

A = []
n = 100
for i in range(n):
    A.append(rnd.randint(1, 6))
    
print(A)

suma = 0
for i in range(len(A)):
    suma += A[i]

media = suma / len(A)
print(media)