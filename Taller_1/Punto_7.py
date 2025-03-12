"""
    
7.) Escribir un programa que determine si un número entero es positivo, negativo o cero. Después,
modificar el programa para que reciba entradas de números enteros hasta que el número introducido
sea 0. El programa debe dar el conteo de positivos y negativos y los respectivos promedios.
    
"""

sumaNegativos, sumaPositivos, conNega, conPosi = 0, 0, 0, 0

while True:
    n = int(input("Ingrese un numero entero = "))
    
    if n < 0:
        sumaNegativos += n
        conNega += 1
    elif n > 1:
        sumaPositivos += n
        conPosi += 1
    else:
        break
        
print(f"""
Se restrijo los siguientes datos

1.) Numeros positivos:
    Suma = {sumaPositivos}
    Cuantos = {conPosi}
    Promedio = {(sumaPositivos / conPosi):.2f}
     
2.) Numeros negativos:
    Suma = {sumaNegativos}
    Cuantos = {conNega}
    Promedio = {(sumaNegativos / conNega):.2f}
      """)