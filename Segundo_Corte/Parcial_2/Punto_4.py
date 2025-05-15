"""

4. Construir un programa que lea un valor n y genere una lista con n
elementos. El programa deberá generar una segunda lista tomando
elementos de a tres en tres posiciones de la lista original

"""

# En estos casos decidi utilizar numpy por su versatilidad y que no sea tan largo
import numpy as np

n = int(input("Ingresa el numero de n para crear una lista aleatoria = "))


def creador_listas(n):
    # Por medio de una funcion propia de crear listas en numpy, similar a la de matrices, se crear una lista random con n datos
    lista = np.random.randint(0, 101, size=n)
    
    # Apartir de una funcion numpy se puede crear una lista dependiendo de los pasos
    new_list = lista[::3]
    
    # Imprimo los resultados
    print(f"""RESULTADOS:
    
    Lista creada = {lista}
    Lista modificada de 3 pasos = {new_list}  
          """)
    
creador_listas(n)