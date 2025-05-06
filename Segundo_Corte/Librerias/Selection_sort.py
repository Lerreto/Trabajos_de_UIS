def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Recorrer la lista hasta el penúltimo elemento
        min_index = i  # Suponemos que el primer elemento es el menor
        for j in range(i + 1, n):  # Buscar el mínimo en la parte restante
            if arr[j] < arr[min_index]:
                min_index = j  # Actualizar el índice del mínimo

        arr[i], arr[min_index] = arr[min_index], arr[i]  # Intercambiar valores
    
    return arr

# Ejemplo de uso
lista = [5, 3, 8, 6, 2]
print("Lista ordenada:", selection_sort(lista))