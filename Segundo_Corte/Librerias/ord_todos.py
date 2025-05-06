import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble_sort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            #operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                #intercambios += 1
        #print(f"paso {i + 1}: {L}")

    return L

def insertion_sort(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            #operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
            #intercambios += 1
            j -= 1
        i += 1
        

    return L

num_elements = np.arange(10, 101, 10)
print(num_elements)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16) # se crea el vector a ordenar
    # acá se hace una copia de ese vector, para preservar el vector con números aleatorios.
    vector_ord = vector.copy()
    # acá viene la estructura para tomar el tiempo
    t_inicio = perf_counter_ns()
    A = bubble_sort(vector_ord) # se ejecuta el método burbuja con el vector copia
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio # se guarda el tiempo para n elementos, para crear una gráfica.
    print(f"Vector ordenado: \n{A}")
    vector_ord = vector.copy() # volvemos a copiar el vector aleatorio original sobre el vector copia para
    # que el siguiente método trabaje sobre los mismos datos
    print(f"Vector sin ordenar: \n{vector_ord}")
    t_inicio = perf_counter_ns()
    A = insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio
    print(A)

print(t_bubble)
print(t_insertion)

plt.plot(num_elements, t_bubble, "g-", num_elements, t_insertion, "b-")
plt.show()