import numpy as np
import math as m

filas = int(input("introduzca el número de filas y columnas, o de ecuaciones: "))
cols = filas

matriz = np.zeros((filas, cols))

for i in range(filas):
    for j in range(cols):
        matriz[i, j] = float(input(f"Introduzca el elemento para la posición {i + 1}, {j + 1} de la matriz: "))

print(matriz)

def datos_matriz(A):
    filas, cols = A.shape
    
    n_filas, n_cols, n_diago = [], [], []
    
    for i in range(filas):
        n_filas.append(list(A[i]))
        n_diago.append(A[i, i])
        n_cols.append(list(A[:, i]))
        
    for x in range(filas, 0, -1):
        n_diago.append(A[i, i])
        
        
    print("Filas:", limpiar_lista(n_filas))
    print("Columnas:", limpiar_lista(n_cols))
    print("Diagonal:", limpiar_diagonal(n_diago)) 
                
def limpiar_lista(lista):
    return [[int(x) if x == int(x) else x for x in fila] for fila in lista]

def limpiar_diagonal(diag):
    return [int(x) if x == int(x) else x for x in diag]

    
datos_matriz(matriz)
   