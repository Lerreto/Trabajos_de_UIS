import numpy as np
from time import perf_counter_ns

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print(A)
print(B)

filasA = len(A)
colsA = len(A[0])
filasB = len(B)
colsB = len(B[0])

C = []

for i in range(filasA):
    temp = []
    for j in range(colsB):
        temp.append(0)
    C.append(temp)


if filasB == colsA:
    for i in range(filasA):
        for j in range(colsB):
            c = 0
            for k in range(filasB):
                c = c + A[i][k] * B[k][j]
                print(f"fila {i}, col {j}, celda {k} - C[{i}][{j}] = {c}")
            C[i][j] = c
            
    print(C)
    
    
# Ahora con numpy

A2 = np.array(A)
B2 = np.array(B)

filasA, colsA = A2.shape
filasB, colsB = B2.shape


C = np.zeros((filasA, colsB))
print(C)

if filasB == colsA:
    for i in range(filasA):
        for j in range(colsB):
            # Manera mas resumida
            # C[i, j] = sum(A2[i, :]*B2[:, j])
            for k in range(colsA):
                C[i, j] = C[i, j] + A2[i, k] * B2[k, j]            
    print(C)
    
# Se puede hacer esto con numpy    
D = A2 @ B2
print(D)

# O esta forma que permite pero solo con igual forma
E = A2 * B2
print(E)