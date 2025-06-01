import numpy as np
from collections import defaultdict

class AdvancedSudokuSolver:
    
    
    """ <----- PARAMETROS INICIALES -----> """
    
    
    def __init__(self):
        # Esto lo puse de medio decorativo, esq parecia vacido con 2 JAJAJAJAJA
        self.size = 9
        self.box_size = 3
        self.grid = None # Almacena la matriz resuelta
        self.candidates = None # Muestra los candidatos posibles
        self.clues = None # Almacena las pistas para determinar dificultad
        self.difficulty = None # La dificultad se define
    
    
    """ <----- HALLANDO CANDIDATOS PARA EL TRABAJO -----> """
     
     
    # En el apartado Grid va a comenzar a guardar todos los candidatos en formato diccionario, de tal manera pueda llamarlos de clave --> valor, pero solo de una casilla
    def get_candidates(self, row, col):
        """Obtiene los candidatos posibles para una celda"""
        if self.grid[row, col] != 0:
            return set()
        
        # Los candidatos los guarda en un set
        used_numbers = set()
        
        # Números usados en la fila
        used_numbers.update(self.grid[row, :])
        
        # Números usados en la columna
        used_numbers.update(self.grid[:, col])
        
        # Números usados en la caja 3x3
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        used_numbers.update(self.grid[box_row:box_row+3, box_col:box_col+3].flatten())
        
        return set(range(1, 10)) - used_numbers
    
    # Recorre todas las casillas del sudoku para llamar luego a la funcion de get_candidates y hallar los candidatos correspondientes
    def update_all_candidates(self):
        """Actualiza la matriz de candidatos para todas las celdas"""
        self.candidates = {}
        self.clues = 0
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    self.candidates[(i, j)] = self.get_candidates(i, j)
                else:
                    self.clues += 1
                    
        if 40 <= self.clues <= 81:
            self.difficulty = "Muy facil"
        elif 35 <= self.clues <= 39:
            self.difficulty  = "Facil"
        elif 30 <= self.clues <= 34:
            self.difficulty  = "Intermedio"
        elif 25 <= self.clues <= 29:
            self.difficulty  = "Dificil"
        elif 22 <= self.clues <= 24:
            self.difficulty  = "Experto"
        elif 17 <= self.clues <= 21:
            self.difficulty  = "Inhumano"
        elif 0 <= self.clues <= 16:
            self.difficulty  = "Hacker"
            
        print(self.difficulty)
    
    
    """ <----- FUNCIONES LOGICAS (TECNICAS SUDOKUS) -----> """
    
    
    # Al recorrer cada casilla si solo tiene un numero de candidato, se establece como dentro de la matriz original
    def naked_singles(self):
        """Técnica: Números desnudos (celdas con un solo candidato)"""
        progress = False
        # Solo hara esta verificacion en la lista de candidatos de los items
        for (row, col), cands in list(self.candidates.items()):
            # Si ve que solamente es uno, lo establece en la matriz grip
            if len(cands) == 1:
                num = list(cands)[0]
                self.grid[row, col] = num
                del self.candidates[(row, col)]
                self.update_candidates_after_placement(row, col, num)
                progress = True
        return progress
    
    def hidden_singles(self):
        """Técnica: Números ocultos (único lugar posible en fila/columna/caja)"""
        progress = False
        
        # Verificar filas y columnas a la vez
        for primary_idx in range(9):
            for num in range(1, 10):
                possible_cols = []
                possible_rows = []
                for secondary_idx in range(9):
                    if (primary_idx, secondary_idx) in self.candidates and num in self.candidates[(primary_idx, secondary_idx)]:
                        possible_cols.append(secondary_idx)
                    if (secondary_idx, primary_idx) in self.candidates and num in self.candidates[(secondary_idx, primary_idx)]:
                        possible_rows.append(secondary_idx)
                
                if len(possible_rows) == 1:
                    secondary_idx = possible_rows[0]
                    key = (secondary_idx, primary_idx)
                    if key in self.candidates:
                        self.grid[secondary_idx, primary_idx] = num
                        del self.candidates[key]
                        self.update_candidates_after_placement(secondary_idx, primary_idx, num)
                        progress = True

                if len(possible_cols) == 1:
                    secondary_idx = possible_cols[0]
                    key = (primary_idx, secondary_idx)
                    if key in self.candidates:
                        self.grid[primary_idx, secondary_idx] = num
                        del self.candidates[key]
                        self.update_candidates_after_placement(primary_idx, secondary_idx, num)
                        progress = True
        
        # Verificar cajas 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for num in range(1, 10):
                    possible_positions = []
                    for r in range(box_row, box_row + 3):
                        for c in range(box_col, box_col + 3):
                            if (r, c) in self.candidates and num in self.candidates[(r, c)]:
                                possible_positions.append((r, c))
                    
                    if len(possible_positions) == 1:
                        row, col = possible_positions[0]
                        self.grid[row, col] = num
                        del self.candidates[(row, col)]
                        self.update_candidates_after_placement(row, col, num)
                        progress = True
        
        return progress
    
    def naked_pairs(self):
        """Técnica: Parejas desnudas (dos celdas con los mismos dos candidatos)"""
        progress = False
        
    # Procesar tanto filas (True) como columnas (False)
        for is_row in [True, False]:
            for primary_idx in range(9):
                # Obtener candidatos de la unidad (fila o columna)
                unit_candidates = {}
                for secondary_idx in range(9):
                    # Determinar coordenadas según si es fila o columna
                    if is_row:
                        pos = (primary_idx, secondary_idx)  # (row, col)
                        key = secondary_idx  # col
                    else:
                        pos = (secondary_idx, primary_idx)  # (row, col)
                        key = secondary_idx  # row
                    
                    if pos in self.candidates and len(self.candidates[pos]) == 2:
                        unit_candidates[key] = self.candidates[pos]
                
                # Agrupar por conjunto de candidatos
                pairs = defaultdict(list)
                for key, cands in unit_candidates.items():
                    pairs[frozenset(cands)].append(key)
                
                # Procesar parejas encontradas
                for cand_set, indices in pairs.items():
                    if len(indices) == 2:  # Pareja encontrada
                        # Eliminar candidatos de otras celdas en la unidad
                        for secondary_idx in range(9):
                            if secondary_idx not in indices:
                                if is_row:
                                    pos = (primary_idx, secondary_idx)
                                else:
                                    pos = (secondary_idx, primary_idx)
                                
                                if pos in self.candidates:
                                    before_len = len(self.candidates[pos])
                                    self.candidates[pos] -= cand_set
                                    if len(self.candidates[pos]) < before_len:
                                        progress = True
        
        # Verificar en cajas 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_candidates = {}
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if (r, c) in self.candidates and len(self.candidates[(r, c)]) == 2:
                            box_candidates[(r, c)] = self.candidates[(r, c)]
                
                pairs = defaultdict(list)
                for pos, cands in box_candidates.items():
                    pairs[frozenset(cands)].append(pos)
                
                for cand_set, positions in pairs.items():
                    if len(positions) == 2:  # Pareja encontrada
                        # Eliminar estos candidatos de otras celdas en la caja
                        for r in range(box_row, box_row + 3):
                            for c in range(box_col, box_col + 3):
                                if (r, c) in self.candidates and (r, c) not in positions:
                                    before_len = len(self.candidates[(r, c)])
                                    self.candidates[(r, c)] -= cand_set
                                    if len(self.candidates[(r, c)]) < before_len:
                                        progress = True
        
        return progress
    
    def pointing_pairs(self):
        """Técnica: Parejas apuntadas (candidatos en una caja que solo están en una fila/columna)"""
        progress = False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for num in range(1, 10):
                    # Encontrar todas las posiciones en la caja donde puede ir este número
                    positions = []
                    for r in range(box_row, box_row + 3):
                        for c in range(box_col, box_col + 3):
                            if (r, c) in self.candidates and num in self.candidates[(r, c)]:
                                positions.append((r, c))
                    
                    if len(positions) >= 2:
                        # Verificar si todas están en la misma fila
                        rows = set(pos[0] for pos in positions)
                        if len(rows) == 1:
                            row = list(rows)[0]
                            # Eliminar este candidato de otras celdas en la fila (fuera de la caja)
                            for c in range(9):
                                if (c < box_col or c >= box_col + 3) and (row, c) in self.candidates:
                                    if num in self.candidates[(row, c)]:
                                        self.candidates[(row, c)].remove(num)
                                        progress = True
                        
                        # Verificar si todas están en la misma columna
                        cols = set(pos[1] for pos in positions)
                        if len(cols) == 1:
                            col = list(cols)[0]
                            # Eliminar este candidato de otras celdas en la columna (fuera de la caja)
                            for r in range(9):
                                if (r < box_row or r >= box_row + 3) and (r, col) in self.candidates:
                                    if num in self.candidates[(r, col)]:
                                        self.candidates[(r, col)].remove(num)
                                        progress = True
        
        return progress
    
    
    """ <----- ACTUALIZACION DESPUES DE CADA PROCESO LOGICO -----> """
    
    
    def update_candidates_after_placement(self, row, col, num):
        """Actualiza candidatos después de colocar un número"""
        # Eliminar de la fila
        for c in range(9):
            if (row, c) in self.candidates:
                self.candidates[(row, c)].discard(num)
        
        # Eliminar de la columna
        for r in range(9):
            if (r, col) in self.candidates:
                self.candidates[(r, col)].discard(num)
        
        # Eliminar de la caja
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if (r, c) in self.candidates:
                    self.candidates[(r, c)].discard(num)
    
    
    """ <----- SOLUCIOND DE SUDOKU POR METODOS LOGICOS -----> """
    
    
    def solve_with_logic(self):
        """Resuelve usando técnicas lógicas avanzadas"""
        self.update_all_candidates()
        
        iteration = 0
        while True:
            iteration += 1
            progress = False
            
            print(f"Iteración {iteration}")
            
            # Aplicar técnicas en orden de simplicidad
            if self.naked_singles():
                print("  ✓ Números desnudos aplicados")
                progress = True
            
            if self.hidden_singles():
                print("  ✓ Números ocultos aplicados")
                progress = True
            
            if self.naked_pairs():
                print("  ✓ Parejas desnudas aplicadas")
                progress = True
            
            if self.pointing_pairs():
                print("  ✓ Parejas apuntadas aplicadas")
                progress = True
            
            # Limpiar candidatos vacíos
            self.candidates = {pos: cands for pos, cands in self.candidates.items() if len(cands) > 0}
            
            if not progress:
                break
            
            # Verificar si está completo
            if len(self.candidates) == 0:
                return True
        
        print(f"Técnicas lógicas completadas en {iteration} iteraciones")
        return len(self.candidates) == 0
    
    
    """ <----- BACKTRACKING -----> """
    
    
    def solve_with_backtrack(self):
        """Backtracking para casos no resueltos por lógica"""
        if len(self.candidates) == 0:
            return True
            
        # Encontrar la celda con menos candidatos (MRV heuristic)
        min_candidates = min(len(cands) for cands in self.candidates.values())
        for (row, col), cands in self.candidates.items():
            if len(cands) == min_candidates:
                break
        
        for num in list(cands):
            # Guardar estado
            old_grid = self.grid.copy()
            old_candidates = {pos: cand_set.copy() for pos, cand_set in self.candidates.items()}
            
            # Hacer movimiento
            self.grid[row, col] = num
            del self.candidates[(row, col)]
            self.update_candidates_after_placement(row, col, num)
            
            # Verificar validez
            valid = all(len(cands) > 0 for cands in self.candidates.values())
            
            if valid and self.solve_with_backtrack():
                return True
            
            # Backtrack
            self.grid = old_grid
            self.candidates = old_candidates
        
        return False
    
    
    """ <----- EJECUCION DEL PROGRAMA POR AMBAS TECNICAS -----> """
    
    
    def solve(self, grid):
        """Método principal de resolución"""
        self.grid = grid.copy()
        
        print("Resolviendo con técnicas lógicas...")
        if self.solve_with_logic():
            print("¡Resuelto completamente con lógica!")
            return True
        
        print(f"Quedan {len(self.candidates)} celdas por resolver")
        print("Aplicando backtracking inteligente...")
        
        if self.solve_with_backtrack():
            print("¡Resuelto con backtracking!")
            return True
        
        return False
    
    
    """ <----- IMPRESION DE MATRIZ EN TERMINAL -----> """
    
    
    def print_grid(self, grid=None):
        """Imprime el sudoku de forma legible"""
        if grid is None:
            grid = self.grid
            
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                
                if j == 8:
                    print(grid[i][j])
                else:
                    print(str(grid[i][j]) + " ", end="")
    
    def print_candidates(self):
        """Imprime los candidatos actuales"""
        print("\nCandidatos restantes:")
        for (row, col), cands in sorted(self.candidates.items()):
            print(f"({row+1},{col+1}): {sorted(list(cands))}")
            

# Funcion que devuelve lo que es el sudoku resuelto y la dificultad
def Resolver(Sudoku_Sin_Resolver):
    
    solver = AdvancedSudokuSolver()
    
    print(f"Sudoku original:")
    solver.print_grid(Sudoku_Sin_Resolver)
    print("\n" + "="*40 + "\n")
    
    if solver.solve(Sudoku_Sin_Resolver):
        print("\nSudoku resuelto:")
        solver.print_grid()
    else:
        print("No se pudo resolver el sudoku")
        solver.print_candidates()
        
    print(f"\nDIFICULTAD: {solver.difficulty}\n")
    
    return solver.grid, solver.difficulty



if __name__ == "__main__":
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

    expert_puzzle_2 = np.array([
        [0, 0, 0, 0, 0, 6, 2, 0, 1],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 2, 0, 0, 7, 0, 5],
        [3, 0, 0, 0, 1, 0, 0, 0, 6],
        [4, 2, 0, 7, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 5, 7, 0, 3, 0, 0, 9, 0],
        [6, 0, 3, 5, 0, 9, 0, 0, 0]
        ])

    Resuelta, dificultad = Resolver(expert_puzzle)
    print(dificultad)