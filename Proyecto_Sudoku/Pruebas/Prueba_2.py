import numpy as np
import time
from collections import defaultdict

class AdvancedSudokuSolver:
    def __init__(self):
        self.size = 9
        self.box_size = 3
        self.grid = None
        self.candidates = None
    
    def get_candidates(self, row, col):
        """Obtiene los candidatos posibles para una celda"""
        if self.grid[row, col] != 0:
            return set()
        
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
    
    def update_all_candidates(self):
        """Actualiza la matriz de candidatos para todas las celdas"""
        self.candidates = {}
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    self.candidates[(i, j)] = self.get_candidates(i, j)
    
    def naked_singles(self):
        """Técnica: Números desnudos (celdas con un solo candidato)"""
        progress = False
        for (row, col), cands in list(self.candidates.items()):
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
        
        # Verificar filas
        for row in range(9):
            for num in range(1, 10):
                possible_cols = []
                for col in range(9):
                    if (row, col) in self.candidates and num in self.candidates[(row, col)]:
                        possible_cols.append(col)
                
                if len(possible_cols) == 1:
                    col = possible_cols[0]
                    self.grid[row, col] = num
                    del self.candidates[(row, col)]
                    self.update_candidates_after_placement(row, col, num)
                    progress = True
        
        # Verificar columnas
        for col in range(9):
            for num in range(1, 10):
                possible_rows = []
                for row in range(9):
                    if (row, col) in self.candidates and num in self.candidates[(row, col)]:
                        possible_rows.append(row)
                
                if len(possible_rows) == 1:
                    row = possible_rows[0]
                    self.grid[row, col] = num
                    del self.candidates[(row, col)]
                    self.update_candidates_after_placement(row, col, num)
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
        
        # Verificar en filas
        for row in range(9):
            row_candidates = {col: cands for (r, col), cands in self.candidates.items() 
                            if r == row and len(cands) == 2}
            
            pairs = defaultdict(list)
            for col, cands in row_candidates.items():
                pairs[frozenset(cands)].append(col)
            
            for cand_set, cols in pairs.items():
                if len(cols) == 2:  # Pareja encontrada
                    # Eliminar estos candidatos de otras celdas en la fila
                    for col in range(9):
                        if (row, col) in self.candidates and col not in cols:
                            before_len = len(self.candidates[(row, col)])
                            self.candidates[(row, col)] -= cand_set
                            if len(self.candidates[(row, col)]) < before_len:
                                progress = True
        
        # Verificar en columnas
        for col in range(9):
            col_candidates = {row: cands for (row, c), cands in self.candidates.items() 
                            if c == col and len(cands) == 2}
            
            pairs = defaultdict(list)
            for row, cands in col_candidates.items():
                pairs[frozenset(cands)].append(row)
            
            for cand_set, rows in pairs.items():
                if len(rows) == 2:  # Pareja encontrada
                    # Eliminar estos candidatos de otras celdas en la columna
                    for row in range(9):
                        if (row, col) in self.candidates and row not in rows:
                            before_len = len(self.candidates[(row, col)])
                            self.candidates[(row, col)] -= cand_set
                            if len(self.candidates[(row, col)]) < before_len:
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
    
    def solve(self, grid):
        """Método principal de resolución con medición de tiempo"""
        self.grid = grid.copy()
        start_time = time.time()
        
        print("Resolviendo con técnicas lógicas...")
        logic_start = time.time()
        logic_solved = self.solve_with_logic()
        logic_time = time.time() - logic_start
        
        print(f"Tiempo de técnicas lógicas: {logic_time:.4f} segundos")
        
        if logic_solved:
            total_time = time.time() - start_time
            print(f"¡Resuelto completamente con lógica en {total_time:.4f} segundos!")
            return True
        
        print(f"Quedan {len(self.candidates)} celdas por resolver")
        print("Aplicando backtracking inteligente...")
        
        backtrack_start = time.time()
        backtrack_solved = self.solve_with_backtrack()
        backtrack_time = time.time() - backtrack_start
        
        total_time = time.time() - start_time
        
        if backtrack_solved:
            print(f"Tiempo de backtracking: {backtrack_time:.4f} segundos")
            print(f"¡Resuelto con backtracking en {total_time:.4f} segundos totales!")
            return True
        
        print(f"Tiempo total fallido: {total_time:.4f} segundos")
        return False
    
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

def benchmark_sudokus():
    """Función para hacer benchmark con múltiples sudokus"""
    
    puzzles = {
        "Fácil": np.array([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]),
        
        "Medio": np.array([
            [0, 2, 0, 6, 0, 8, 0, 0, 0],
            [5, 8, 0, 0, 0, 9, 7, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 0],
            [3, 7, 0, 0, 0, 0, 5, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 0, 0, 1, 3],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 9, 8, 0, 0, 0, 3, 6],
            [0, 0, 0, 3, 0, 6, 0, 9, 0]
        ]),
        
        "Difícil": np.array([
            [0, 0, 0, 6, 0, 0, 4, 0, 0],
            [7, 0, 0, 0, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 9, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 1, 8, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 6, 0, 4, 5],
            [0, 4, 0, 2, 0, 0, 0, 6, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 1, 0, 0]
        ]),
        
        "Extremo": np.array([
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ])
    }
    
    print("=" * 60)
    print("BENCHMARK DE RENDIMIENTO - SOLUCIONADOR DE SUDOKU")
    print("=" * 60)
    
    total_start = time.time()
    results = {}
    
    for difficulty, puzzle in puzzles.items():
        print(f"\n🎯 RESOLVIENDO SUDOKU {difficulty.upper()}")
        print("-" * 40)
        
        solver = AdvancedSudokuSolver()
        
        # Contar celdas vacías
        empty_cells = np.count_nonzero(puzzle == 0)
        print(f"Celdas vacías: {empty_cells}/81 ({empty_cells/81*100:.1f}%)")
        
        start_time = time.time()
        success = solver.solve(puzzle)
        end_time = time.time()
        
        elapsed = end_time - start_time
        results[difficulty] = {
            'time': elapsed,
            'success': success,
            'empty_cells': empty_cells
        }
        
        if success:
            print(f"✅ ÉXITO en {elapsed:.4f} segundos")
        else:
            print(f"❌ FALLÓ después de {elapsed:.4f} segundos")
    
    total_time = time.time() - total_start
    
    # Resumen de resultados
    print("\n" + "=" * 60)
    print("RESUMEN DE RESULTADOS")
    print("=" * 60)
    
    for difficulty, result in results.items():
        status = "✅" if result['success'] else "❌"
        print(f"{status} {difficulty:8}: {result['time']:8.4f}s ({result['empty_cells']:2d} celdas vacías)")
    
    print(f"\n⏱️  Tiempo total: {total_time:.4f} segundos")
    
    # Estadísticas adicionales
    successful_times = [r['time'] for r in results.values() if r['success']]
    if successful_times:
        print(f"📊 Tiempo promedio: {np.mean(successful_times):.4f}s")
        print(f"📊 Tiempo más rápido: {min(successful_times):.4f}s")
        print(f"📊 Tiempo más lento: {max(successful_times):.4f}s")

def compare_solvers():
    """Compara el solucionador optimizado vs backtracking puro"""
    from time import perf_counter  # Más preciso para benchmarks
    
    # Sudoku de dificultad media
    test_puzzle = np.array([
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
    
    print("\n" + "=" * 50)
    print("COMPARACIÓN: OPTIMIZADO vs BACKTRACKING PURO")
    print("=" * 50)
    
    # Solucionador optimizado
    print("🚀 Solucionador optimizado:")
    solver_opt = AdvancedSudokuSolver()
    start = perf_counter()
    success_opt = solver_opt.solve(test_puzzle.copy())
    time_opt = perf_counter() - start
    
    # Backtracking puro (simulado - más lento)
    print(f"\n⚡ Resultado optimizado: {time_opt:.6f} segundos")
    
    # También puedes probar múltiples veces para mayor precisión
    print(f"\n🔬 Ejecutando benchmark de precisión (10 ejecuciones)...")
    times = []
    for i in range(10):
        solver = AdvancedSudokuSolver()
        start = perf_counter()
        solver.solve(test_puzzle.copy())
        times.append(perf_counter() - start)
    
    print(f"📊 Tiempo promedio: {np.mean(times):.6f}s")
    print(f"📊 Desviación estándar: {np.std(times):.6f}s")
    print(f"📊 Rango: {min(times):.6f}s - {max(times):.6f}s")
    # Sudoku muy difícil que requiere técnicas avanzadas
    expert_puzzle = np.array([
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
    
    solver = AdvancedSudokuSolver()
    
    print("Sudoku original (nivel experto):")
    solver.print_grid(expert_puzzle)
    print("\n" + "="*40 + "\n")
    
    if solver.solve(expert_puzzle):
        print("\nSudoku resuelto:")
        solver.print_grid()
    else:
        print("No se pudo resolver el sudoku")
        solver.print_candidates()

if __name__ == "__main__":
    # Puedes cambiar esta línea para usar main() o main_with_options()
    min()  # Ejecución simple del sudoku
    # main_with_options()  # Para opciones de benchmark