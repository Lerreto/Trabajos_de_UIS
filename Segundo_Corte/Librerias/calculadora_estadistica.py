"""

Calcular desviación estándar, media, variancia y rango

"""

import random as rnd
from tabulate import tabulate

def crear_lista():
    vals = []
    n = int(input("Ingrese el numero de datos para hacer los calculos: "))
    print()
    for x in range(n):
        vals.append(rnd.randint(18, 60)) 
        
    return vals   

# Media
def media(lista_vals:list):
    return sum(lista_vals) / len(lista_vals)

# Varianza poblacional
def varianza_poblacional(lista_vals:list):
    sum_vari = 0
    promedio = media(lista_vals)
    for x in lista_vals:
        sum_vari += ((x - promedio)**2)

    return sum_vari / len(lista_vals)

# Varianza estandar poblacional
def varianza_estandar(lista_vals:list):
    return varianza_poblacional(lista_vals) ** 0.5

def maxmin(lista_vals):
    return max(lista_vals), min(lista_vals)

# Rango
def rango(lista_vals:list):
    max , min = maxmin(lista_vals)
    return  max - min

# Mensaje personalizado
def mensaje(lista_vals:list):
    max, min = maxmin(lista_vals)
    
    return f"""

Segun la tabla anterior:

LIMITES :
    Max Valor = {max}
    Min Valor = {min}
    Rango = {rango(lista_vals)}
    
PROMEDIO :
    Numero de datos = {len(lista_vals)}
    Media = {media(lista_vals):.2f}

VARIACIONES :
    Variacion Poblacional = {(varianza_poblacional(lista_vals)):.2f}
    Variacion Estandar = {(varianza_estandar(lista_vals)):.2f}

"""

# Imprimir la tabla
def tabla(lista_vals:list):
    # Definir el número de columnas
    columnas = 5  

    # Crear la tabla dividiendo la lista en filas
    filas = [vals[i:i + columnas] for i in range(0, len(lista_vals), columnas)]

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

# Declaro lista
vals = crear_lista()

# Tabla que necesito
tabla(vals)

# Imprimiendo el texto
print(mensaje(vals))