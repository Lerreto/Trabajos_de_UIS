"""
    
1. Construir un programa que obtenga el promedio de los valores de los
elementos de la diagonal principal y la secundaria de una matriz
cuadrada de n x n; los elementos de la matriz son generados de manera
aleatoria entre 0 y 99, y el valor n debe ser pedido al usuario. (Nota:
recordar que el módulo random permite generar números aleatorios, y
también que numpy tiene sus propios generadores de aleatorios)
    
"""

import numpy as np

# Para crear la matriz le pido al usuario un valor n, que representa el tamaño
n = int(input("introduzca el numero de matriz n x n: "))
i, j = n, n # Establezco lo que es columnas y filas
matriz = np.random.randint(0, 100, size=(i, j)) # Es una funcion propia de numpy
print(matriz)

# Esta es la propia funcion que calcula la matriz
def cal_diagonal(A):
    filas, cols = A.shape
    dia_pri, dia_sec = 0, 0 # Esto es para guardar la suma correspondiente
    
    # Recorre i veces dependiendo del tamaño de la matriz
    for i in range(filas):
        dia_pri += A[i, i]
        dia_sec += A[(i), (filas - (i + 1))] # la matriz secundarialo q varia es la segunda
        
    print(f"""\nRESULTADOS:
          
    Diagonal Princiapal = {dia_pri / filas}
    Diagonal Secundaria = {dia_sec / filas}""")

                
cal_diagonal(matriz)