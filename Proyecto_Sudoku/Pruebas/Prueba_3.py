import numpy as np

class SudokuSolver:
    def __init__(self):
        self.size = 9
        self.box_size = 3
    
    def is_valid(self, grid, row, col, num):
        """
        Verifica si es válido colocar un número en una posición específica
        """
        # Verificar fila
        if num in grid[row, :]:
            return False
        
        # Verificar columna
        if num in grid[:, col]:
            return False
        
        # Verificar caja 3x3
        box_row = (row // self.box_size) * self.box_size
        box_col = (col // self.box_size) * self.box_size
        
        if num in grid[box_row:box_row + self.box_size, box_col:box_col + self.box_size]:
            return False
        
        return True
    
    def find_empty_cell(self, grid):
        """
        Encuentra la primera celda vacía (con valor 0)
        """
        empty_cells = np.where(grid == 0)
        if len(empty_cells[0]) > 0:
            return empty_cells[0][0], empty_cells[1][0]
        return None, None
    
    def solve(self, grid):
        """
        Resuelve el sudoku usando backtracking
        """
        row, col = self.find_empty_cell(grid)
        
        # Si no hay celdas vacías, el sudoku está resuelto
        if row is None:
            return True
        
        # Intentar números del 1 al 9
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row, col] = num
                
                # Recursión
                if self.solve(grid):
                    return True
                
                # Backtrack
                grid[row, col] = 0
        
        return False
    
    def print_grid(self, grid):
        """
        Imprime el sudoku de forma legible
        """
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                
                if j == 8:
                    print(grid[i][j])
                else:
                    print(str(grid[i][j]) + " ", end="")
    
    def is_valid_sudoku(self, grid):
        """
        Verifica si un sudoku es válido (sin resolver necesariamente)
        """
        for i in range(self.size):
            for j in range(self.size):
                if grid[i, j] != 0:
                    num = grid[i, j]
                    grid[i, j] = 0  # Temporalmente vacía para verificar
                    if not self.is_valid(grid, i, j, num):
                        grid[i, j] = num  # Restaurar
                        return False
                    grid[i, j] = num  # Restaurar
        return True

def main():
    # Ejemplo de sudoku (0 representa celdas vacías)
    sudoku_puzzle = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])
    
    solver = SudokuSolver()
    
    print("Sudoku original:")
    solver.print_grid(sudoku_puzzle)
    print("\n" + "="*25 + "\n")
    
    # Crear una copia para resolver
    puzzle_copy = sudoku_puzzle.copy()
    
    if solver.solve(puzzle_copy):
        print("Sudoku resuelto:")
        solver.print_grid(puzzle_copy)
    else:
        print("No se pudo resolver el sudoku")
    
    # Ejemplo adicional: sudoku más difícil
    print("\n" + "="*40 + "\n")
    print("Sudoku más difícil:")
    
    hard_puzzle = np.array([
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ])
    
    solver.print_grid(hard_puzzle)
    print("\n" + "="*25 + "\n")
    
    hard_copy = hard_puzzle.copy()
    if solver.solve(hard_copy):
        print("Sudoku difícil resuelto:")
        solver.print_grid(hard_copy)
    else:
        print("No se pudo resolver el sudoku difícil")

if __name__ == "__main__":
    main()