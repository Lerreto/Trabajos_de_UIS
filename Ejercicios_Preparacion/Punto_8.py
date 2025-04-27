def entero_a_romano(n):
    # Mapeo de números romanos
    valores = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    romano = ''
    
    for valor, simbolo in valores:
        while n >= valor:
            romano += simbolo
            n -= valor
            
    return romano

# Bucle para pedir números
while True:
    numero = int(input("Introduce un número entero positivo (0 para terminar): "))
    if numero == 0:
        break
    elif numero > 0:
        print(f"El número {numero} en romano es: {entero_a_romano(numero)}")
    else:
        print("Por favor, introduce un número positivo.")