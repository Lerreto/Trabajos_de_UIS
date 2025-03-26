"""

Calcular desviación estándar, media, variancia y rango

"""

import random as rnd
from tabulate import tabulate

vals = []
n = int(input("Ingrese el numero de datos para hacer los calculos: "))
print()
for x in range(n):
    vals.append(rnd.randint(18, 60))
    
n = len(vals)

# Definir el número de columnas
columnas = 5  

# Crear la tabla dividiendo la lista en filas
filas = [vals[i:i + columnas] for i in range(0, n, columnas)]

# Imprimir el título
print("=" * 22)
print("   TABLA DE VALORES")
print("=" * 22)

# Imprimir encabezado de columnas
header = " | ".join(f"C{i+1}" for i in range(columnas))
print(header)
print("-" * len(header))

# Imprimir los valores alineados
for fila in filas:
    print(" | ".join(f"{num:2}" for num in fila))
    
# Media
suma_vals = 0
for i in vals:
    suma_vals += i
    
media = suma_vals / n

# Varianza poblacional
sum_vari = 0
for x in vals:
    sum_vari += ((x - media)**2)

varianza = sum_vari / n

# Varianza estandar poblacional
vari_estandar = varianza ** 0.5

# Rango
maxvals = vals[0]
minvals = vals[0]

for h in vals:
    if h < minvals:
        minvals = h
        
    if h > maxvals:
        maxvals = h
        
rango = maxvals - minvals
    
    
# Imprimiendo el texto

mensaje = f"""

Segun la tabla anterior:

LIMITES :
    Max Valor = {maxvals}
    Min Valor = {minvals}
    Rango = {rango}
    
PROMEDIO :
    Numero de datos = {n}
    Media = {media:.2f}

VARIACIONES :
    Variacion Poblacional = {varianza:.2f}
    Variacion Estandar = {vari_estandar:.2f}

"""

print(mensaje)