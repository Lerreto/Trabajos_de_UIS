import tkinter as tk
from tkinter import messagebox
import numpy as np
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
        
        # Verificar en columnas y cajas (código similar omitido por brevedad)
        return progress
    
    def pointing_pairs(self):
        """Técnica: Parejas apuntadas"""
        progress = False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for num in range(1, 10):
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
                            for c in range(9):
                                if (c < box_col or c >= box_col + 3) and (row, c) in self.candidates:
                                    if num in self.candidates[(row, c)]:
                                        self.candidates[(row, c)].remove(num)
                                        progress = True
                        
                        # Verificar si todas están en la misma columna
                        cols = set(pos[1] for pos in positions)
                        if len(cols) == 1:
                            col = list(cols)[0]
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
        
        while True:
            progress = False
            
            if self.naked_singles():
                progress = True
            
            if self.hidden_singles():
                progress = True
            
            if self.naked_pairs():
                progress = True
            
            if self.pointing_pairs():
                progress = True
            
            # Limpiar candidatos vacíos
            self.candidates = {pos: cands for pos, cands in self.candidates.items() if len(cands) > 0}
            
            if not progress:
                break
            
            if len(self.candidates) == 0:
                return True
        
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
        """Método principal de resolución"""
        self.grid = np.array(grid, dtype=int)
        
        if self.solve_with_logic():
            return True
        
        if self.solve_with_backtrack():
            return True
        
        return False

def checker(valor):
    if valor == "":
        return True
    return valor == "" or (valor.isdigit() and 1 <= int(valor) <= 9)

def resolver():
    global sudokutemp
    # Crear matriz del sudoku actual
    sudoku = []
    for fila in sudokutemp:
        fila_valores = []
        for entrada in fila:
            valor = entrada.get()
            if valor == "":
                fila_valores.append(0)
            else:
                fila_valores.append(int(valor))
        sudoku.append(fila_valores)
    
    print("Sudoku a resolver:")
    for fila in sudoku:
        print(fila)
    
    # Crear el solucionador y resolver
    solver = AdvancedSudokuSolver()
    
    try:
        if solver.solve(sudoku):
            # Actualizar la interfaz con la solución
            solucion = solver.grid
            for i in range(9):
                for j in range(9):
                    sudokutemp[i][j].delete(0, tk.END)
                    sudokutemp[i][j].insert(0, str(solucion[i][j]))
            
            messagebox.showinfo("¡Éxito!", "¡Sudoku resuelto correctamente!")
            print("Sudoku resuelto:")
            for fila in solucion:
                print(fila)
        else:
            messagebox.showerror("Error", "No se pudo resolver el sudoku. Verifica que sea válido.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error al resolver: {str(e)}")

def limpiar():
    """Limpia todas las celdas del sudoku"""
    global sudokutemp
    for fila in sudokutemp:
        for entrada in fila:
            entrada.delete(0, tk.END)

def cargar_ejemplo():
    """Carga un sudoku de ejemplo"""
    global sudokutemp
    ejemplo = [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ]
    
    for i in range(9):
        for j in range(9):
            sudokutemp[i][j].delete(0, tk.END)
            if ejemplo[i][j] != 0:
                sudokutemp[i][j].insert(0, str(ejemplo[i][j]))

def reiniciar():
    ventana.destroy()
    main()

def main():
    global ventana, sudokutemp
    ventana = tk.Tk()
    ventana.title("Sudokapp - Solucionador Avanzado")
    ventana.geometry('700x550')
    ventana.resizable(False, False)
    
    vf = ventana.register(checker)
    
    # Título
    titulo = tk.Label(ventana, text="Sudoku Solver", font=('Arial', 20, 'bold'))
    titulo.pack(pady=10)
    
    # Frame para el tablero
    tablero_frame = tk.Frame(ventana)
    tablero_frame.pack(pady=10)
    
    sudokutemp = []
    for row in range(9):
        filasu = []
        for col in range(9):
            # Bordes para separar las cajas 3x3
            if row % 3 == 0:
                top_bor = 5
            else:
                top_bor = 1
            if col % 3 == 0:
                left_bor = 5
            else:
                left_bor = 1
            
            caja = tk.Entry(  
                tablero_frame,
                width=2,
                relief="solid",
                font=('Arial', 18),
                validate="key",
                bd=1,
                validatecommand=(vf, "%P"),
                justify='center'
            )
           
            caja.grid(row=row, column=col, padx=(left_bor,0), pady=(top_bor, 0))
            filasu.append(caja)
           
        sudokutemp.append(filasu)
    
    # Frame para los botones
    botones_frame = tk.Frame(ventana)
    botones_frame.pack(pady=20)
    
    boton_resolver = tk.Button(botones_frame, text="Resolver", bd=3, command=resolver, 
                              font=('Arial', 12), bg='lightgreen', width=10)
    boton_limpiar = tk.Button(botones_frame, text="Limpiar", bd=3, command=limpiar, 
                             font=('Arial', 12), bg='lightblue', width=10)
    boton_ejemplo = tk.Button(botones_frame, text="Ejemplo", bd=3, command=cargar_ejemplo, 
                             font=('Arial', 12), bg='lightyellow', width=10)
    boton_reiniciar = tk.Button(botones_frame, text="Reiniciar", bd=3, command=reiniciar, 
                               font=('Arial', 12), bg='lightcoral', width=10)
    
    # Organizar botones en una fila
    boton_resolver.grid(row=0, column=0, padx=5)
    boton_limpiar.grid(row=0, column=1, padx=5)
    boton_ejemplo.grid(row=0, column=2, padx=5)
    boton_reiniciar.grid(row=0, column=3, padx=5)
    
    # Instrucciones
    instrucciones = tk.Label(ventana, text="Ingresa los números del 1-9. Deja vacías las celdas desconocidas.", 
                            font=('Arial', 10))
    instrucciones.pack(pady=5)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()