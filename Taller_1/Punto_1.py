"""

1.) Construir un programa que lea un número variable de valores enteros. El resultado que entregara el
programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores
pares dividida por el número de estos.

"""

dato = ""
suma = 0
contandor = 0

while True:
    
    dato = int(input("Ingrese el numero entero par (0 para salir) = "))
    
    if dato == 0:
        break

    if type(dato) == int and dato % 2 == 0:
        suma += dato
        contandor += 1

    else:
        print("\nADVERTENCIA = Debes de ingresar un numero par\n")

print(f"El promedio seria de: {(suma/contandor):.2f}")