"""

3.) Escribir un programa que lea un número entero y determine cuales de sus
cifras son pares y cuales son impares. Además, el programa debe contar cuantas
cifras tiene el número en total.

"""

# Esto es mas de decoracion para que se vea bonito
print("-" * 20 + " Punto 3 " + "-" * 20)

# Pido n para hallar las cifras y un contador casero
n, contador_casero_sin_Len_Porque_Si = input("\nIngrese un numero entero largo en su preferencia = "), 0

# Tambien es decorativo y para verse mejor
print(f"\nDentro del numero {n} las cifras estan clasificadas en: \n")

# En cada cifra verifico si es par o impar, al estar en str puedo iterar mas facil y luego lo paso a int
for x in n:
    if int(x) % 2 == 0:
        print(f"La cifra numero {contador_casero_sin_Len_Porque_Si} la cual es {x} es: Par")
    else:
        print(f"La cifra numero {contador_casero_sin_Len_Porque_Si} la cual es {x} es: Impar")

    # Y con el contador casero se lo agrego 1
    contador_casero_sin_Len_Porque_Si += 1

# Agrego o muestro el contador de cifras casero     
print(f"\nEl numero {n} tiene un total de {contador_casero_sin_Len_Porque_Si} Cifras")