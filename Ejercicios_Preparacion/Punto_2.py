"""

2. Construir un programa que tome una cadena de caracteres e imprima todas la posibles permutaciones de los mismos. Antes de construirlas, el programa deberá limpiar posibles caracteres repetidos de la cadena. Se deberá obtener un número N de elementos que se toman, y se debe tener en cuenta el número M de posibles valores, es decir, el número de caracteres diferentes en la cadena dada. Por ejemplo:

cadena de entrada: abcfga
elementos que se tienen en cuenta: abcfg
permutaciones:
abcfg
abcgf
abgfc
…

El programa deberá imprimir todas las posibles permutaciones, que se entienden como todos los posibles ordenamientos del conjunto de caracteres que resulta de la limpieza de la cadena dada. Cada permutación se debe convertir en una cadena de texto a la hora de presentar los resultados.

"""



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