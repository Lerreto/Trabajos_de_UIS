"""

2. Construir un programa que lea una lista de elementos enteros de
longitud n (n debe ser pedida al usuario) y calcule el promedio de los
elementos en posiciones pares y la suma de los elementos en las
posiciones impares de la lista. También debe crear una segunda lista
en la que se guarden los valores resultantes de dividir los elementos en
las posiciones pares por el máximo de los elementos y los impares por
el mínimo. Mostrar todos los resultados en pantalla.

"""

# En estos casos decidi utilizar numpy por su versatilidad y que no sea tan largo
import numpy as np

n = int(input("Ingresa el numero de n para crear una lista aleatoria = "))

# Por medio de una funcion propia de crear listas en numpy, similar a la de matrices, se crear una lista random con n datos
lista = np.random.randint(0, 101, size=n)
print(lista)

# Funcion que hace los procesos
def promedio_posicion(A):
    Impares = sum(A[::2]) # Funcion de numpy que guarda los numeros que esten en posiciones impares, esto lo hace señalando los pasos, iniciando desde la posicion 0 para el programa, 1 para nosotros, y asi va saltando de 2 en 2
    Pares = sum(A[1::2]) # Es la misma que la anterior pero inicia en la posicion en 2 y procede con los saltos
    new_list_pares = A[1::2] / np.max(A) # Es el mismo proceso que el anterior, pero en vez de sumarlo, se dividen los elemntos por el maixmo, cosa que no necesita map, que es para las listas
    
    # En dado caso que el minimo sea 0, se va por el segundo menor
    if np.min(A) == 0:
        new_list_impares = A[::2] / np.partition(A, 1)[1] # Lo que hace el np.partition, organiza la lista de menor a mayor, seguidamente escojo el segundo menor, osea en la posicion 1
    else:
        new_list_impares = A[::2] / np.min(A) # Si no se sigue lo mismo usando el menor numero de la lista
    
    # Imprimo los valores
    print(f"""RESULTADOS
    
    Lista = {A}
    
    Impares = {A[::2]}
    Pare = {A[1::2]}
    
    Suma de impares = {Impares}
    Suma de pares = {Pares}
    
    Nueva lista Pares = {new_list_pares}
    Nueva lista Impares = {new_list_impares}  
          
    """)
    
promedio_posicion(lista)

