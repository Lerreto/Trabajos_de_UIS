"""

1.) Construir un programa que lea un número variable de valores enteros. El resultado que entregara el
programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores
pares dividida por el número de estos.

"""

mensaje = True
dato = ""
suma = 0
contandor = 0

while mensaje:
    
    dato = int(input("Ingrese el numero entero par (-1 para salir) = "))

    if type(dato) == int and dato % 2 == 0:
        suma += dato
        contandor += 1

    elif dato == -1:
        mensaje = False

    else:
        print("\nADVERTENCIA = Debes de ingresar un numero par\n")

print(f"El promedio seria de: {(suma/contandor):.2f}")