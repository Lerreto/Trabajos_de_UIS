import sys
import os

# Agrega la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora ya puedes importar los módulos de Logic correctamente
from Logic.Generate_Sudoku import generar_sudoku_jugable
from Logic.Solve_Sudoku import Resolver
from Logic.Verifi_Sudoku import verificacion

sudoku = generar_sudoku_jugable()
print(sudoku)

Resolver(sudoku)