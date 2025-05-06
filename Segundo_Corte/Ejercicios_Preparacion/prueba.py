def entero_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    resultado = ""

    for i in range(len(valores)):
        while numero >= valores[i]:
            resultado += romanos[i]
            numero -= valores[i]

    return resultado

# Bucle principal
while True:
    try:
        numero = int(input("Introduce un número entero positivo (0 para salir): "))
        if numero == 0:
            print("Programa finalizado.")
            break
        elif numero < 0:
            print("Por favor, introduce solo números positivos.")
        else:
            romano = entero_a_romano(numero)
            print(f"{numero} en números romanos es: {romano}")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")