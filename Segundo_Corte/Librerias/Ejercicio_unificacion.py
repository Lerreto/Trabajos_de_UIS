import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
import random as rnd

#? Mensajes personalizados para hacer el menu mas accesible
mensaje_bienvenida = ("""
          
    BIENVENIDOS AL MENU DE GRAFICACION
    
    REGLAS:
    
    1.) Va a ser basada en 3 metodos, bubble, insertion, selection
    2.) Crear una lista para graficar (1)
    3.) Reglas basicas o este mensaje (2)
    4.) Salir (0)
          
          """)

mensaje_graficar = ("""
          
    ACCIONES:
    
    1.) Graficar en funcion de cuanto tiempo demoro (1)
    2.) Graficar en funcion de las operaciones (2)
    3.) Reglas basicas o este mensaje (3)
    4.) Salir (0)
          
          """)

#? Aqui estan los metodos de ordenamiento para poder hacer luego las graficas
#! Bubble sort
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

#! Insertion sort
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

#! Selection sort
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

#? Operador de tiempo para evitar tanto codigo repetido
def operaciones_tiemnpo(Metodo, lista_ran, i, t_metodo, ops_metodo):

    vector_ord = lista_ran.copy()
    t_inicio = perf_counter_ns()
    datico = Metodo(vector_ord)
    t_final = perf_counter_ns()
    ops_metodo[i] = datico
    t_metodo[i] = t_final - t_inicio
    
    return t_metodo, ops_metodo
    

def contador_segundos():
    
    t_bubble = np.zeros(size)
    ops_bubble = np.zeros(size)
    t_insertion = np.zeros(size)
    ops_selection = np.zeros(size)
    t_selection = np.zeros(size)
    ops_insertion = np.zeros(size)

    
    for i, n in enumerate(num_elements) :
        vector = np.random.randint(0, 100, n, dtype=np.int16)
        
        t_bubble, ops_bubble = operaciones_tiemnpo(bubble_sort, vector, i, t_bubble, ops_bubble)
        t_selection, ops_selection = operaciones_tiemnpo(selection_sort, vector, i, t_selection, ops_selection)
        t_insertion, ops_insertion = operaciones_tiemnpo(insertion_sort, vector, i, t_insertion, ops_insertion)

        
    return t_bubble, t_insertion, t_selection, ops_bubble, ops_insertion, ops_selection


def grafica_segundos():
    bubble, selection, insertion, op_bubble, op_insertion, op_selection = contador_segundos()

    print(mensaje_graficar)
    
    while True:
        
        condicion = int(input("Ahora necesito que ingreses que accion hacer (0 para salir) = "))
        
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
            plt.plot(num_elements, op_bubble, "g-", label="Bubble Sort")
            plt.plot(num_elements, op_insertion, "r-", label="Selection Sort")
            plt.plot(num_elements, op_selection, "b-", label="Insertion Sort")

            # Añadir título y etiquetas a los ejes
            plt.title('Comparación de Operaciones en Ejecución de Algoritmos de Ordenamiento')
            plt.xlabel('Operaciones')
            plt.ylabel('Operaciones')

            # Añadir leyenda
            plt.legend()

            # Mostrar el gráfico
            plt.show()
            
        elif condicion == 3:
            print(mensaje_graficar)
            
        else:
            break


#? Estructura basica para inicializacion de graficas, que no es necesario ejecutarlo mas de 1 vez
num_elements = np.arange(10, 101, 10)
size = num_elements.size

#? Aqui simplemente se ejecuta todo que es una simple funcion
print(mensaje_bienvenida)
while True:
    number = int(input("Ingrese la accion que desea realizar = "))
    
    if number == 1:
        grafica_segundos()
    
    elif number == 2:
        print(mensaje_bienvenida)
        
    else:
        break
    