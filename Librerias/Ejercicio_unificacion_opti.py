import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
import random as rnd

# Mensajes para opciones de menú
MENSAJE_BIENVENIDA = """
          
    BIENVENIDOS AL MENU DE GRAFICACION
    
    REGLAS:
    
    1.) Va a ser basada en 3 metodos, bubble, insertion, selection
    2.) Crear una lista para graficar (1)
    3.) Reglas basicas o este mensaje (2)
    4.) Salir (0)
          
"""

MENSAJE_GRAFICAR = """
          
    ACCIONES:
    
    1.) Graficar en funcion de cuanto tiempo demoro (1)
    2.) Graficar en funcion de las operaciones (2)
    3.) Reglas basicas o este mensaje (3)
    4.) Salir (0)
          
"""

# Algoritmos de ordenamiento con conteo de operaciones
def bubble_sort(arr):
    operaciones = 0
    n = len(arr)
    # Crear una copia para evitar modificar el original
    L = arr.copy()
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            operaciones += 1  # Operación de comparación
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                operaciones += 1  # Operación de intercambio

    return operaciones

def insertion_sort(arr):
    operaciones = 0
    # Crear una copia para evitar modificar el original
    L = arr.copy()
    
    for i in range(1, len(L)):
        clave = L[i]
        j = i - 1
        operaciones += 1  # Comparación inicial
        
        while j >= 0 and L[j] > clave:
            L[j + 1] = L[j]
            operaciones += 1  # Operación de asignación
            j -= 1
            
        L[j + 1] = clave
    
    return operaciones

def selection_sort(arr):
    operaciones = 0
    # Crear una copia para evitar modificar el original
    L = arr.copy()
    
    for i in range(len(L) - 1):
        indice_min = i
        for j in range(i + 1, len(L)):
            operaciones += 1  # Operación de comparación
            if L[indice_min] > L[j]:
                indice_min = j
                
        if indice_min != i:
            L[indice_min], L[i] = L[i], L[indice_min]
            operaciones += 1  # Operación de intercambio

    return operaciones

# Función para medir el tiempo de ejecución y contar operaciones
def medir_algoritmo(funcion_ordenamiento, datos, indice, array_tiempo, array_ops):
    # No es necesario copiar aquí ya que estamos copiando dentro de cada función de ordenamiento
    tiempo_inicio = perf_counter_ns()
    operaciones = funcion_ordenamiento(datos)
    tiempo_fin = perf_counter_ns()
    
    array_tiempo[indice] = tiempo_fin - tiempo_inicio
    array_ops[indice] = operaciones
    
    return array_tiempo, array_ops

def ejecutar_mediciones(num_elementos, tamano):
    # Inicializar arrays para resultados
    tiempos = {
        'bubble': np.zeros(tamano),
        'insertion': np.zeros(tamano),
        'selection': np.zeros(tamano)
    }
    
    operaciones = {
        'bubble': np.zeros(tamano),
        'insertion': np.zeros(tamano),
        'selection': np.zeros(tamano)
    }
    
    # Ejecutar mediciones para cada tamaño de entrada
    for i, n in enumerate(num_elementos):
        # Generar un array aleatorio una vez para cada tamaño
        datos = np.random.randint(0, 100, n, dtype=np.int16)
        
        # Medir cada algoritmo con los mismos datos
        tiempos['bubble'], operaciones['bubble'] = medir_algoritmo(
            bubble_sort, datos, i, tiempos['bubble'], operaciones['bubble'])
        
        tiempos['insertion'], operaciones['insertion'] = medir_algoritmo(
            insertion_sort, datos, i, tiempos['insertion'], operaciones['insertion'])
        
        tiempos['selection'], operaciones['selection'] = medir_algoritmo(
            selection_sort, datos, i, tiempos['selection'], operaciones['selection'])
    
    return tiempos, operaciones

def graficar_resultados(datos_x, datos_y, titulo, etiqueta_x, etiqueta_y, nombres_algoritmos):
    plt.figure(figsize=(10, 6))
    
    colores = ['g-', 'b-', 'r-']
    
    for i, algo in enumerate(nombres_algoritmos):
        plt.plot(datos_x, datos_y[algo], colores[i], label=f"Sort {algo.capitalize()}")
    
    # Añadir título y etiquetas
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    # Añadir leyenda y cuadrícula para mejor legibilidad
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Mostrar la gráfica
    plt.show()

def menu_visualizacion(num_elementos, tiempos, operaciones):
    nombres_algoritmos = ['bubble', 'insertion', 'selection']
    
    print(MENSAJE_GRAFICAR)
    
    while True:
        try:
            opcion = int(input("Ahora necesito que ingreses que accion hacer (0 para salir) = "))
            
            if opcion == 1:
                # Graficar tiempos de ejecución
                graficar_resultados(
                    num_elementos, 
                    tiempos, 
                    'Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento',
                    'Número de elementos',
                    'Tiempo de ejecución (ns)',
                    nombres_algoritmos
                )
                
            elif opcion == 2:
                # Graficar conteo de operaciones
                graficar_resultados(
                    num_elementos, 
                    operaciones, 
                    'Comparación de Operaciones en Ejecución de Algoritmos de Ordenamiento',
                    'Número de elementos',
                    'Número de operaciones',
                    nombres_algoritmos
                )
                
            elif opcion == 3:
                print(MENSAJE_GRAFICAR)
                
            elif opcion == 0:
                break
                
            else:
                print("Opción no válida. Intente de nuevo.")
                
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    # Definir el rango de elementos a probar
    num_elementos = np.arange(10, 101, 10)
    tamano = len(num_elementos)
    
    print(MENSAJE_BIENVENIDA)
    
    while True:
        try:
            opcion = int(input("Ingrese la accion que desea realizar = "))
            
            if opcion == 1:
                # Ejecutar mediciones y recopilar resultados
                tiempos, operaciones = ejecutar_mediciones(num_elementos, tamano)
                # Mostrar menú de visualización
                menu_visualizacion(num_elementos, tiempos, operaciones)
                
            elif opcion == 2:
                print(MENSAJE_BIENVENIDA)
                
            elif opcion == 0:
                print("Gracias por usar el programa. ¡Hasta pronto!")
                break
                
            else:
                print("Opción no válida. Intente de nuevo.")
                
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()