import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
import random as rnd


# Bubble sort
def bubble_sort(L:list):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            #operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                #intercambios += 1

    return L

# Insertion sort
def insertion_sort(L:list):
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

# Selection sort
def selection_sort(L:list):
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            #operaciones += 1
            if (L[min] > L[j]):
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
            #intercambios += 1
            #operaciones += 1

    return L

# Estructura basica
def bubble_sort(A):
    return 0

num_elements = np.arange(1000, 100001, 1000)
size = num_elements.size
print(size)
#print(num_elements)
t_cositas = np.zeros(size)

def contador_segundos(metodo):
    for i, n in enumerate(num_elements) :
        vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
        t_inicio = perf_counter_ns()
        metodo(vector_ord)
        t_final = perf_counter_ns()
        t_cositas[i] = t_final - t_inicio

    return t_cositas


bubble = contador_segundos(bubble_sort)
selection = contador_segundos(selection_sort)
insertion = contador_segundos(insertion_sort)

plt.plot(num_elements, bubble, "g-", num_elements, selection, "r-", num_elements, insertion, "b-")
plt.show()