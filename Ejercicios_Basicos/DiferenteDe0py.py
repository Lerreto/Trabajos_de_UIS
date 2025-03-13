salir = False

while salir != True:
    n = int(input("Numero: "))
    if n == 0:
        print("Es igual a 0")
        salir = True
    elif n > 0:
        print("Es positivo")
    else:
        print("Es negativo")