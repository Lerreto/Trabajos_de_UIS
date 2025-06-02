import numpy as np

#Matriz que se tomará de ejemplo para rectificar (Se puede modificar)
expert_puzzle = np.array([
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ])


'''Función que rectificará si hay algún elemento repetido en una fila, columna o 
   cuadrado (Llamando a la respectiva función en el último caso)'''
   
def rectificar(matriz):
    cuad = rectsqr(matriz)
   
    
    if cuad == False:
         return False
    

    for i in range(9):
        for j in range(9):
            A = matriz[i]
            B = matriz[:, j]
     
            if matriz[i,j] != 0:
                print(matriz[i,j])
                A_new = np.delete(A, j)
                B_new = np.delete(B, i)
                print(A)
                print(B)
  
                for x in range(len(A_new)):
                    if matriz[i,j] == A_new[x]:
                        return False
                for x in range(len(B_new)):
                    if matriz[i,j] == B_new[x]:
                        return False
            
    return True
    
    
#Función que rectifica si alguno de los 9 cuadrados 3x3 en el Sudoku posee elementos repetidos en este mismo
def rectsqr(matriz):
    
    #Ciclos que pasarán por las filas y columnas en saltos de 3 en 3
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            numeros = []
            for q in range(i,i+3):
                for k in range(j,j+3):
                    if matriz[q,k] != 0:
                        numeros.append(matriz[q,k])
            numeros = np.array(numeros)
            numeros_unicos = np.unique(numeros)
            print(f"Unico {numeros_unicos}\n no único {numeros}")
            if len(numeros) != len(numeros_unicos):
                return False
                        
                                        
    return True



estado = rectificar(expert_puzzle)

#Si alguna de las condiciones devuelve el resultado "False", se asume que hay algún elemento repetido
if estado == False:
    print("El Sudoku tiene elementos repetidos en alguna fila, columna o cuadrado")

#Al contrario, entonces se asume que el sudoku está bien estructurado    
else:
    print("El Sudoku no tiene elementos repetidos que Infrinja las reglas")
