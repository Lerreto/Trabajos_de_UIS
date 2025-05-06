"""
    
6.) Escribir un programa que reciba una entrada n, que es un número entero. El programa devolverá una
lista de números enteros hasta n, incluyéndolo, y especificando si el número es divisible por 2, 3 o por
5, o si es divisible por ambos. Por ejemplo, asumiendo una entrada n=18:

1
2. Divisible por 2
3. Divisible por 3
4 Divisible por 2
5. Divisible por 5
6. Divisible por 2 y 3
7
8. Divisible por 2
9. Divisible por 3
10. Divisible por 2 y 5
11
12. Divisible por 2 y 3
13.
14. Divisible por 2.
15. Divisible por 3 y 5
16. Divisible por 2
17
18. Divisible por 2 y 3

"""

n = int(input("Ingrese un número entero: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(f"{i}. Divisible por 2, 3 y 5")
    elif i % 2 == 0 and i % 3 == 0:
        print(f"{i}. Divisible por 2 y 3")
    elif i % 2 == 0 and i % 5 == 0:
        print(f"{i}. Divisible por 2 y 5")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i}. Divisible por 3 y 5")
    elif i % 2 == 0:
        print(f"{i}. Divisible por 2")
    elif i % 3 == 0:
        print(f"{i}. Divisible por 3")
    elif i % 5 == 0:
        print(f"{i}. Divisible por 5")
    else:
        print(i)
        
print("\nOtra manera de hacerlo:\n")


for i in range(1, n + 1):
    message = f"{i}"
    divisors = []
        
    if i % 2 == 0:
        divisors.append("2")
    if i % 3 == 0:
        divisors.append("3")
    if i % 5 == 0:
        divisors.append("5")
        
    if divisors:
        message += f". Divisible por {' y '.join(divisors)}"
        
    print(message)