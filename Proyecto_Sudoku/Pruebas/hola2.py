import tkinter as tk
import numpy as np



sudoku = np.array([
    [0, 8, 0, 5, 7, 6, 2, 0, 0],
    [0, 0, 0, 4, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 3, 9, 5, 4, 8],
    [6, 3, 0, 9, 0, 0, 8, 5, 2],
    [0, 9, 0, 2, 0, 0, 3, 7, 0],
    [8, 0, 0, 0, 5, 0, 6, 9, 4],
    [2, 5, 7, 6, 0, 3, 4, 8, 9],
    [3, 0, 8, 7, 0, 0, 0, 2, 5],
    [0, 4, 0, 0, 0, 0, 0, 0, 6]
]) 

tam = np.shape(sudoku)[0]





while True:

    for i in range(0, tam, 3):
        for j in range(0, tam, 3):
            doubles = []
            posiciones = []
            for g in range(i, i+3):
                for m in range(j, i+3):
                    if sudoku[g, m] == 0:
                        pos = [g, m]
                        lista = list(range(1, 10))
                        doubles.append(lista)
                        posiciones.append(pos)               
            print(np.array(doubles))
            print(np.array(posiciones))



