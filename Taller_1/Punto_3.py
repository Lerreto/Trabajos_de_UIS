"""

3.) Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro
entero, o sea, que tiene raíz cuadrada entera.

"""
while True:

    n = int(input("\nIngrese un numero entero ( -1 para salir): "))

    if n == -1:
        break

    if n == 0:
        print("Debes de ingresar un numero mayor a 0")
    else:
        dato = n ** 0.5
        if n % dato == 0:
            print(f"El numero {n} tiene raiz cuadrada entera que es {int(dato)}")
        else:
            print(f"El numero {n} no tiene una raiz cuadrada entera")