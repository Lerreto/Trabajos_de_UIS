import numpy as np
import random

def generar_sudoku_base():
    base = 3
    lado = base * base

    def patron(fila, columna):
        return (base * (fila % base) + fila // base + columna) % lado

    def mezcla(grupo):
        return random.sample(grupo, len(grupo))

    filas = [g * base + r for g in mezcla(range(base)) for r in mezcla(range(base))]
    columnas = [g * base + c for g in mezcla(range(base)) for c in mezcla(range(base))]
    numeros = mezcla(range(1, lado + 1))

    tablero = np.array([[numeros[patron(f, c)] for c in columnas] for f in filas])
    return tablero

def quitar_casillas(tablero, nivel='intermedio'):
    sudoku = tablero.copy()
    if nivel == 'facil':
        pistas = random.randint(28, 35)
    elif nivel == 'intermedio':
        pistas = random.randint(22, 27)
    elif nivel == 'dificil':
        pistas = random.randint(15, 21)
    else:
        pistas = 40  # por defecto

    # Total de celdas = 81, eliminar el resto
    casillas_a_borrar = 81 - pistas
    posiciones = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(posiciones)

    for i in range(casillas_a_borrar):
        fila, col = posiciones[i]
        sudoku[fila][col] = 0

    return sudoku

def generar_sudoku_jugable(nivel='intermedio'):
    solucion = generar_sudoku_base()
    sudoku_con_espacios = quitar_casillas(solucion, nivel)
    return sudoku_con_espacios

# Ejemplo de uso
if __name__ == "__main__":
    sudoku = generar_sudoku_jugable(nivel='intermedio')
    print(sudoku)
