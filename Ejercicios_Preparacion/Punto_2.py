def limpiar_cadena(palabra):
    cadena_devolver = []
    for x in palabra:
        if x not in cadena_devolver:
            cadena_devolver.append(x)
    
    return cadena_devolver

def generar_permutaciones(lista, n, perm_actual="", usadas=None):
    if usadas is None:
        usadas = [False] * len(lista)

    if len(perm_actual) == n:
        print(perm_actual)
        return

    for i in range(len(lista)):
        if not usadas[i]:
            usadas[i] = True
            generar_permutaciones(lista, n, perm_actual + lista[i], usadas)
            usadas[i] = False  # backtracking


cadena = input("Ingrese la cadena de caracteres: ")
N = int(input("¿Cuántos elementos quieres tomar para las permutaciones?: "))

# Limpiar caracteres repetidos
caracteres_unicos = limpiar_cadena(cadena)
M = len(caracteres_unicos)

print(f"\nElementos únicos ({M}): {caracteres_unicos}")

if N > M:
    print("Error: no puedes tomar más caracteres de los que hay disponibles.")
else:
    print(f"\nPermutaciones de longitud {N}:")
    generar_permutaciones(caracteres_unicos, N)