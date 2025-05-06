def limpiar_cadena(palabra):
    cadena_devolver = []
    for x in palabra:
        if x not in cadena_devolver:
            cadena_devolver.append(x)
    
    return cadena_devolver

def permutation(s):
   if len(s) == 1:
     return [s]

   perm_list = []
   for a in s:
     remaining_elements = [x for x in s if x != a]
     z = permutation(remaining_elements)

     for t in z:
       perm_list.append([a] + t)

   return perm_list


cadena = input("Ingrese la cadena de caracteres: ")

# Limpiar caracteres repetidos
caracteres_unicos = limpiar_cadena(cadena)

print(f"\nElementos únicos : {caracteres_unicos}")

permutaciones = permutation(caracteres_unicos)
for x in permutaciones:
    contatenado = "".join(x)
    print(contatenado)
