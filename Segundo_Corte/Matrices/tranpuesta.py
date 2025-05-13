import numpy as np
import math as m

filas = int(input("introduzca el número de filas y columnas, o de ecuaciones: "))
cols = filas

matriz = np.zeros((filas, cols))

for i in range(filas):
    for j in range(cols):
        matriz[i, j] = float(input(f"Introduzca el elemento para la posición {i + 1}, {j + 1} de la matriz: "))

print(matriz)

def transpuesta(A):
    filas, cols = A.shape
    matriz_trans = np.zeros((filas, cols))
    
    for i in range(filas):
        for x in range(filas):
            matriz_trans[x, i] = A[i, x]
            
    print(matriz_trans)
            
transpuesta(matriz)
        