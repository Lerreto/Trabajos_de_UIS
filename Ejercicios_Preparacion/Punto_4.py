"""

4. Un número es un cuadrado perfecto si su raíz cuadrada es un número exacto (sin decimales). Por ejemplo, el 4 es un cuadrado perfecto (2²), al igual que lo son el 36 (6²) y el 3.500.641 (1871²).

Todos los números que no son cuadrados perfectos pueden multiplicarse por otros para conseguir serlo. Por ejemplo, el número 8 no es un cuadrado perfecto, pero al multiplicarlo por 2 se obtiene el 16, que sí lo es.

Entradas del programa: La entrada comienza con un número que indica cuántos casos de prueba tendrán que procesarse. Cada caso de prueba consiste en un número mayor que 0 y menor que  2 a la 31.

Salidas: Para cada caso de prueba, el programa escribirá por la salida estándar, en una línea independiente, el número más pequeño que al ser multiplicado por el número del caso de prueba da como resultado uncuadrado perfecto.     
    
"""

def determinar_multiplicador(n):
    factores_n = []
    divisor = 2
    multiplicar = 1
    
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            factores_n.append(divisor)
        else:
            divisor += 1
    
    for x in set(factores_n):
        if factores_n.count(x) % 2 != 0:
            multiplicar *= x
        
    return multiplicar
        

def determinar_cuadrado(numero):
    if numero <= 0 or numero >= 2 ** 31:
        return f"El número {numero} no cumple con el requisito de ser mayor que 0 y menor que 2³¹."

    raiz = numero ** 0.5

    if raiz.is_integer():
        return f"{numero} x 1 = {numero} : Raiz cuadrada = {int(raiz)}"
    else:
        multiplicador = determinar_multiplicador(numero)
        nuevo_numero = numero * multiplicador
        nueva_raiz = int(nuevo_numero ** 0.5)
        return f"{numero} x {multiplicador} = {nuevo_numero} : Raiz cuadrada = {nueva_raiz}"
    
numeros = [4, 6, 36, 3500641, 65, 21, 45, 0]
for x in numeros:
    mensaje = determinar_cuadrado(x)
    print(mensaje)
