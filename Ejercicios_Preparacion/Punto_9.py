def encontrar_pares(lista, objetivo):
    vistos = set()  # Conjunto para almacenar los números ya vistos
    pares = set()   # Conjunto para almacenar los pares únicos encontrados
    
    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            # Crear el par ordenado (min, max) para evitar duplicados como (1, 6) y (6, 1)
            par = tuple(sorted((num, complemento)))
            pares.add(par)
        vistos.add(num)
    
    # Imprimir todos los pares únicos
    for par in pares:
        print(par[0], par[1])

# Ejemplo de uso
lista = [1, 2, 3, 4, 3, 5, 6, 7, 8]
objetivo = 10
encontrar_pares(lista, objetivo)