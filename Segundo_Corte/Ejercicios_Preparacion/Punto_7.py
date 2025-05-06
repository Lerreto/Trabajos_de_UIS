def es_triangulor_superior(matriz, n):
    for i in range(n):
        for j in range(i):
            if matriz[i][j] != 0:
                return False
    return True

def es_triangulor_inferior(matriz, n):
    for i in range(n):
        for j in range(i+1, n):

            if matriz[i][j] != 0:
                return False
    return True

def es_triangulor(matriz, n):
    print(matriz)
    # Verificar si es triangular superior o inferior
    if es_triangulor_superior(matriz, n) or es_triangulor_inferior(matriz, n):
        return "SI"
    else:
        return "NO"

while True:
    n = int(input("Ingre la numero de la matriz = "))
    if n == 0:
        break

    # Leer la matriz
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    
    # Verificar si la matriz es triangular
    print(es_triangulor(matriz, n))