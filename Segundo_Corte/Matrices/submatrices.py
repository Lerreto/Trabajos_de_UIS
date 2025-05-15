import numpy as np

def extraer_submatrices(matriz, tamano_submatriz):
    """
    Extrae todas las submatrices de tamaño m×m posibles de una matriz.
    
    Args:
        matriz: La matriz principal (numpy array 2D)
        tamano_submatriz: Tamaño m de las submatrices cuadradas a extraer
        
    Returns:
        Una lista de todas las submatrices posibles
    """
    if not isinstance(matriz, np.ndarray):
        matriz = np.array(matriz)
    
    filas, columnas = matriz.shape
    
    if tamano_submatriz > filas or tamano_submatriz > columnas:
        raise ValueError("El tamaño de submatriz especificado es mayor que la matriz original")
    
    submatrices = []
    
    # Recorremos la matriz original
    for i in range(filas - tamano_submatriz + 1):
        for j in range(columnas - tamano_submatriz + 1):
            # Extraer la submatriz
            submatriz = matriz[i:i+tamano_submatriz, j:j+tamano_submatriz]
            submatrices.append(submatriz)
    
    return submatrices

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una matriz de ejemplo 5x5
    matriz_ejemplo = np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])
    
    print("Matriz original:")
    print(matriz_ejemplo)
    
    # Extraer submatrices 2x2
    tamano_submatriz = 2
    submatrices = extraer_submatrices(matriz_ejemplo, tamano_submatriz)
    
    print(f"\nSubmatrices {tamano_submatriz}x{tamano_submatriz} extraídas:")
    for i, submatriz in enumerate(submatrices):
        print(f"Submatriz {i+1}:")
        print(submatriz)
    
    # Extraer submatrices 3x3
    tamano_submatriz = 3
    submatrices = extraer_submatrices(matriz_ejemplo, tamano_submatriz)
    
    print(f"\nSubmatrices {tamano_submatriz}x{tamano_submatriz} extraídas:")
    for i, submatriz in enumerate(submatrices):
        print(f"Submatriz {i+1}:")
        print(submatriz)