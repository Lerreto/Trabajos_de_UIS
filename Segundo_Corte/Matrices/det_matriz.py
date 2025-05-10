import numpy as np
import math

def calcular_determinante_manual(matriz):
    """
    Calcula el determinante de una matriz n x n usando el método de expansión por cofactores
    
    Args:
        matriz: Una matriz numpy n x n
    
    Returns:
        El valor del determinante
    """
    n = len(matriz)
    
    # Caso base: matriz 1x1
    if n == 1:
        return matriz[0, 0]
    
    # Caso base: matriz 2x2
    if n == 2:
        return matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
    
    # Para matrices más grandes, usamos expansión por cofactores
    determinante = 0
    for j in range(n):
        # Creamos la submatriz eliminando la primera fila y la columna j
        submatriz = np.delete(np.delete(matriz, 0, axis=0), j, axis=1)
        # Sumamos el cofactor (alternando signo)
        cofactor = matriz[0, j] * calcular_determinante_manual(submatriz) * (-1) ** j
        determinante += cofactor
    
    return determinante

def main():
    try:
        # Solicitar el tamaño de la matriz
        n = int(input("Ingrese el tamaño de la matriz (n): "))
        
        if n <= 0:
            print("El tamaño de la matriz debe ser un número positivo.")
            return
        
        # Crear una matriz vacía
        matriz = np.zeros((n, n))
        
        # Ingresar los elementos de la matriz
        print(f"\nIngrese los elementos de la matriz {n}x{n}:")
        for i in range(n):
            for j in range(n):
                matriz[i, j] = float(input(f"Elemento [{i+1},{j+1}]: "))
        
        # Mostrar la matriz ingresada
        print("\nLa matriz ingresada es:")
        for i in range(n):
            print("[", end=" ")
            for j in range(n):
                if matriz[i, j] == int(matriz[i, j]):
                    print(f"{int(matriz[i, j])}", end=" ")
                else:
                    print(f"{matriz[i, j]:.2f}", end=" ")
            print("]")
        
        # Calcular y mostrar el determinante manualmente
        det = calcular_determinante_manual(matriz)
        
        # Redondear a cero si está muy cerca a cero
        if abs(det) < 1e-10:
            det = 0
        
        # Verificar si es prácticamente un entero
        if abs(det - round(det)) < 1e-10:
            det = round(det)
        
        print("\nEl determinante de la matriz es:", end=" ")
        if det == int(det):
            print(int(det))
        else:
            print(f"{det:.4f}")
        
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()