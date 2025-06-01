import numpy as np  # Biblioteca para trabajar con matrices de forma eficiente
import random       # Biblioteca para operaciones aleatorias

# Función que genera un tablero de Sudoku completamente resuelto
def generar_sudoku_base():
    base = 3               # Tamaño de los bloques (3x3)
    lado = base * base     # Lado del tablero (9x9)

    # Define el patrón para llenar la cuadrícula con una solución válida
    def patron(fila, columna):
        return (base * (fila % base) + fila // base + columna) % lado

    # Mezcla aleatoriamente los elementos de un grupo
    def mezcla(grupo):
        return random.sample(grupo, len(grupo))

    # Genera un orden aleatorio de filas, columnas y números usando el patrón
    filas = [g * base + r for g in mezcla(range(base)) for r in mezcla(range(base))]
    columnas = [g * base + c for g in mezcla(range(base)) for c in mezcla(range(base))]
    numeros = mezcla(range(1, lado + 1))

    # Construye el tablero completo aplicando el patrón a la disposición aleatoria
    tablero = np.array([[numeros[patron(f, c)] for c in columnas] for f in filas])
    return tablero  # Devuelve un Sudoku completamente resuelto

# Función que quita casillas del Sudoku para convertirlo en un juego jugable
def quitar_casillas(tablero):
    # Selecciona aleatoriamente un nivel de dificultad
    nivel = random.choice(["Muy facil", "Facil", "Intermedio", "Dificil", "Experto", "Inhumano", "Hacker"])

    sudoku = tablero.copy()  # Copia el tablero completo para no modificar el original

    # Determina el número de pistas iniciales según el nivel de dificultad
    if nivel == 'Muy facil':
        pistas = random.randint(40, 81)
    elif nivel == 'Facil':
        pistas = random.randint(35, 39)
    elif nivel == 'Intermedio':
        pistas = random.randint(30, 34)
    elif nivel == 'Dificil':
        pistas = random.randint(25, 29)
    elif nivel == 'Experto':
        pistas = random.randint(22, 24)
    elif nivel == 'Inhumano':
        pistas = random.randint(17, 21)
    elif nivel == 'Hacker':
        pistas = random.randint(5, 16)

    # Calcula cuántas casillas deben borrarse (el total es 81)
    casillas_a_borrar = 81 - pistas

    # Genera una lista de todas las posiciones del tablero y la mezcla aleatoriamente
    posiciones = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(posiciones)

    # Borra (pone en 0) las casillas necesarias para alcanzar el número deseado de pistas
    for i in range(casillas_a_borrar):
        fila, col = posiciones[i]
        sudoku[fila][col] = 0

    print(f"Nivel del sudoku: {nivel}")  # Muestra el nivel seleccionado
    return sudoku  # Devuelve el Sudoku con espacios en blanco para jugar

# Función que genera un Sudoku jugable, con solución incluida
def generar_sudoku_jugable():
    solucion = generar_sudoku_base()           # Genera un tablero completo
    sudoku_con_espacios = quitar_casillas(solucion)  # Le quita casillas según la dificultad
    return sudoku_con_espacios  # Devuelve el tablero listo para jugar

# Ejemplo de uso
if __name__ == "__main__":
    sudoku = generar_sudoku_jugable()
    print(sudoku)
