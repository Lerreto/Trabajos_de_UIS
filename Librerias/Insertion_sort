def insertion_sort(arr):
    for i in range(1, len(arr)):  # Empezamos desde el segundo elemento (índice 1)
        key = arr[i]  # Elemento actual a comparar
        j = i - 1  # Índice del elemento anterior
        
        # Mover los elementos mayores a la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Insertar el elemento en su posición correcta
    
    return arr  # Retornar el array ordenado

# Ejemplo de uso
lista = [12, 11, 13, 5, 6, 6, 7, 8, 9]
print("Lista ordenada:", insertion_sort(lista))