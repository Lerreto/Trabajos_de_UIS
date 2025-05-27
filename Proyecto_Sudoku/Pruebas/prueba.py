import numpy as np

# Sudoku #1 como matriz NumPy
# 0 representa las celdas vacías
sudoku = np.array([
    [0, 8, 0, 5, 7, 6, 2, 0, 0],
    [0, 0, 0, 4, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 3, 9, 5, 4, 8],
    [6, 3, 0, 9, 0, 0, 8, 5, 2],
    [0, 9, 0, 2, 0, 0, 3, 7, 0],
    [8, 0, 0, 0, 5, 0, 6, 9, 4],
    [2, 5, 7, 6, 0, 3, 4, 8, 9],
    [3, 0, 8, 7, 0, 0, 0, 2, 5],
    [0, 4, 0, 0, 0, 0, 0, 0, 6]
])

solucion_sudoku = np.array([
    [9, 8, 4, 5, 7, 6, 2, 1, 3],
    [5, 1, 3, 4, 8, 2, 9, 6, 7],
    [7, 2, 6, 1, 3, 9, 5, 4, 8],
    [6, 3, 1, 9, 4, 7, 8, 5, 2],
    [4, 9, 5, 2, 6, 8, 3, 7, 1],
    [8, 7, 2, 3, 5, 1, 6, 9, 4],
    [2, 5, 7, 6, 1, 3, 4, 8, 9],
    [3, 6, 8, 7, 9, 4, 1, 2, 5],
    [1, 4, 9, 8, 2, 5, 7, 3, 6]
])


print("Sudoku original:")
print(sudoku)
print()

# Función para mostrar el sudoku de forma más legible
def mostrar_sudoku(matriz):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if matriz[i][j] == 0:
                print(".", end=" ")
            else:
                print(matriz[i][j], end=" ")
        print()

print("Sudoku formateado:")
mostrar_sudoku(sudoku)

# Información sobre la matriz
print(f"\nDimensiones: {sudoku.shape}")
print(f"Tipo de datos: {sudoku.dtype}")
print(f"Celdas vacías: {np.count_nonzero(sudoku == 0)}")
print(f"Celdas llenas: {np.count_nonzero(sudoku != 0)}")