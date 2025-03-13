"""

5.) Escribir un programa que permita convertir un entero dado en base 2, 4, 8, 16.

"""

n = int(input("Ingrese un numero entero: "))
base = ""
m = 1

while m != 16:
    
    m *= 2
    x = n
    base = ""
    cadena = "ABCDEF"
    
    while x != 0:
        residuo = x % m
        x = x // m
        
        if residuo >= 10:
            posicion = residuo - 10
            residuo = cadena[posicion]
            
        base = str(residuo) + base 
    
    if m == 16:
        base = "0x" + base
    
    print(f"El numero {n} en base {m} = {base}")
    