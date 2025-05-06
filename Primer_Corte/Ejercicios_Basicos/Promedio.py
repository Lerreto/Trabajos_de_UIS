n = int(input("Numero de elementos: "))
suma = 0
for i in range(n):
    elem = float(input(f"Valor del elemnto {i}: "))
    suma = suma + elem
    
if n > 0:
    promedio = suma / n
    print(f"{promedio:.2f}")
    