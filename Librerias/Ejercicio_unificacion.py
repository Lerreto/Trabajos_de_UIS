import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
import random as rnd

mensaje_bienvenida = ("""
          
    BIENVENIDOS AL MENU DE GRAFICACION
    
    REGLAS:
    
    1.) Va a ser basada en 3 metodos, bubble, insertion, selection
    2.) Graficar cuanto duran los metodos en orden en base a la lista (1)
    3.) Graficar el numero de operaciones y intercambios (2)
    4.) Reglas basicas o este mensaje (3)
    4.) Salir (Cualquier cosa)
          
          """)

# Bubble sort
def bubble_sort(L:list):
    
    operaciones = 0
    
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                operaciones += 1

    return operaciones

# Insertion sort
def insertion_sort(L:list):
    
    operaciones = 0
    
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            L[j], L[j - 1] = L[j - 1], L[j]
            operaciones += 1
            j -= 1
        i += 1

    return operaciones

# Selection sort
def selection_sort(L:list):
    
    operaciones = 0
    
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            operaciones += 1
            if (L[min] > L[j]):
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
            operaciones += 1

    return operaciones

def operaciones_tiemnpo(Metodo, lista_ran, i):
    

    vector_ord = lista_ran.copy()
    t_inicio = perf_counter_ns()
    datico = Metodo(vector_ord)
    t_final = perf_counter_ns()
    ops_metodo[i] = datico
    t_metodo[i] = t_final - t_inicio
    
    return ops_metodo, t_metodo
    

def contador_segundos():
    
    t_bubble = np.zeros(size)
    ops_bubble = np.zeros(size)
    t_insertion = np.zeros(size)
    ops_selection = np.zeros(size)
    t_selection = np.zeros(size)
    ops_insertion = np.zeros(size)
    
    for i, n in enumerate(num_elements) :
        vector = np.random.randint(0, 100, n, dtype=np.int16)
        
        t_bubble, ops_bubble = operaciones_tiemnpo(bubble_sort, vector, i)
        t_selection, ops_selection = operaciones_tiemnpo(selection_sort, vector, i)
        t_insertion, ops_insertion = operaciones_tiemnpo(insertion_sort, vector, i)

        
    return t_bubble, t_insertion, t_selection, ops_bubble, ops_insertion, ops_selection


def grafica_segundos(condicion):
    bubble, selection, insertion, ops_bubble, ops_insertion, ops_selection = contador_segundos()

    if condicion == 1:
        # Graficar los resultados
        plt.plot(num_elements, bubble, "g-", label="Bubble Sort")
        plt.plot(num_elements, selection, "r-", label="Selection Sort")
        plt.plot(num_elements, insertion, "b-", label="Insertion Sort")

        # Añadir título y etiquetas a los ejes
        plt.title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento')
        plt.xlabel('Número de elementos')
        plt.ylabel('Tiempo de ejecución (ns)')

        # Añadir leyenda
        plt.legend()

        # Mostrar el gráfico
        plt.show()
        
    elif condicion == 2:
        # Graficar los resultados
        plt.plot(num_elements, ops_bubble, "g-", label="Bubble Sort")
        plt.plot(num_elements, ops_selection, "r-", label="Selection Sort")
        plt.plot(num_elements, ops_insertion, "b-", label="Insertion Sort")

        # Añadir título y etiquetas a los ejes
        plt.title('Comparación de Operaciones en Ejecución de Algoritmos de Ordenamiento')
        plt.xlabel('Operaciones')
        plt.ylabel('Operaciones')

        # Añadir leyenda
        plt.legend()

        # Mostrar el gráfico
        plt.show()


# Estructura basica para inicializacion de graficas
num_elements = np.arange(10, 101, 10)
#print(num_elements)
size = num_elements.size
#print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
ops_bubble = np.zeros(size)
ops_selection = np.zeros(size)
ops_insertion = np.zeros(size)

print(mensaje_bienvenida)

while True:
    number = int(input("Ingrese la accion que desea realizar = "))
    
    if number == 1:
        grafica_segundos(1)
        
    elif number == 2:
        grafica_segundos(2)
    
    elif number == 3:
        print(mensaje_bienvenida)
        
    else:
        break
    