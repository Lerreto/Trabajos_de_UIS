"""

1.) Escribir un programa que lea un número entero y determine si este es un
palíndromo, es decir, que se lee igual de izquierda a derecha que de derecha a
izquierda. Estos números se conocen como como capicúas.

12321, 454, 555, etc.

Nota: asumir que el número dado no tendrá ceros a la derecha

"""

# Esto es mas decorativo indicando que es el primer punto
print("-" * 20 + " Punto 1 " + "-" * 20)

# Pido un numero entero para poder determinar la condicion
numero = input("\nDebes de ingresar un numero entero: ")

# El [::-1] es un funcion propia de python que permite invertir las cadenas al reves o incluso lista, su sintaxis seria: iterable[inicio:fin:paso]

# En la condicion pido que si el numero en str (para mejor manipulacion) es igual a la invertida, si es asi se retorna eso, si no, no es
if numero == numero[::-1]:
    print(f"\nEl numero {numero} Es palindromo")
else:
    print(f"\nEl numero {numero} no es palindromo")


# Otra manera de hacerlo sin el [::-1]
print("\n" + "-" * 20 + " Otra Manera " + "-" * 20)

# Pido nuevamente el numero
numero = input("\nDebes de ingresar un numero entero: ")

# Aqui almcenare la cadena inversa
numero_inverso = ""

# Invirtiendo la cadena por medio del for
for x in numero:
    numero_inverso = x + numero_inverso

# Verifico si son iguales, si no es asi no es palindromo
if numero == numero_inverso:
    print(f"\nEl numero {numero} Es palindromo")
else:
    print(f"\nEl numero {numero} no es palindromo")