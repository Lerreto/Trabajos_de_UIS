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

def númerosolo(A, B, C):
    doublessimp = []
    convun = []
    temptam = np.shape(A)[0]
    for p in range():
        listatemp = []
        listatemp = np.setdiff1d(A[p], C[0])
        listatemp = np.setdiff1d(listatemp[0], sudoku[(B[p, 0])])
        listatemp = np.setdiff1d(listatemp[0], sudoku[:, (B[p], 1)])
        doublessimp.append(listatemp)
    
    doublessimp2 = np.array(doublessimp)
    
    par = np.array(list(range(1,10)))
    
    for q in range(temptam):
        par = np.intersect1d(par[0], doublessimp2[q])
    
    print(f"El par para el bloque es: {par}")
    
    
    parapp = np.array(list(par))
     
    for F in range(temptam):
        if F < temptam-2:
            conum = np.setdiff1d(doublessimp2[F], parapp[0])
            np.append(parapp, conum[0])
            convun.append(conum[0])
        else:
            convun.append(conum[0])
    
    return convun
            
        
        
        
        
        

while True:

    for i in range(0, tam, 3):
        for j in range(0, tam, 3):
            doubles = []
            posiciones = []
            descartados = []
            for g in range(i, i+3):
                for m in range(j, i+3):
                    if sudoku[g, m] == 0:
                        pos = [g, m]
                        lista = list(range(1, 10))
                        doubles.append(lista)
                        posiciones.append(pos)
                    else:
                        descartados.append(sudoku[g, m])
                               
            númerosolo(np.array(doubles), np.array(posiciones), np.array(descartados))                    
            print(np.array(doubles))
            print(np.array(posiciones))


