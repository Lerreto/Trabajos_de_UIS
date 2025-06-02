import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import sys
import os

# Agrega la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ============================================================================
# AQUÍ DEBES IMPORTAR TUS MÓDULOS REALES:
# ============================================================================

from Logic.Generate_Sudoku import generar_sudoku_jugable
from Logic.Solve_Sudoku import Resolver
from Logic.Verifi_Sudoku import verificacion


# ============================================================================
# CLASE PRINCIPAL DE LA APLICACIÓN
# ============================================================================
class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Solucionario de Sudokus")
        self.root.configure(bg='#1e1e1e')
        self.root.geometry("1000x750")  # Aumentado el tamaño
        
        # Centrar ventana en pantalla
        self.center_window()
        
        # Matriz de sudoku (9x9) inicializada en ceros
        self.sudoku_matrix = np.zeros((9, 9), dtype=int)
        
        # Variables para la interfaz
        self.entries = []
        self.dificultad_var = tk.StringVar(value="Ninguna")
        
        # Variable para evitar verificaciones múltiples - mejorada
        self.verificando = False
        self.error_mostrado = False
        
        self.setup_styles()
        self.create_widgets()
    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def setup_styles(self):
        """Configurar estilos personalizados"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para botones principales - más grandes y con hover
        style.configure('Modern.TButton',
                       background='#404040',
                       foreground='white',
                       borderwidth=2,
                       focuscolor='none',
                       font=('Arial', 12, 'bold'),  # Fuente más grande
                       relief='flat',
                       padding=(20, 10))  # Más padding
        
        style.map('Modern.TButton',
                  background=[('active', '#00ff44'),  # Verde al hacer hover
                            ('pressed', '#00cc33')],
                  foreground=[('active', 'black'),    # Texto negro en hover
                            ('pressed', 'black')],
                  relief=[('pressed', 'flat'),
                         ('!pressed', 'flat')])
        
        # Estilo para labels - más grandes
        style.configure('Modern.TLabel',
                       background='#1e1e1e',
                       foreground='white',
                       font=('Arial', 16, 'bold'))  # Fuente más grande
        
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal con mejor padding
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Título principal más grande
        title_label = tk.Label(main_frame, 
                              text="🧩 Solucionario de Sudokus",
                              font=('Arial', 28, 'bold'),  # Mucho más grande
                              bg='#1e1e1e',
                              fg='#00ff88')
        title_label.pack(pady=(0, 30))
        
        # Frame contenedor horizontal centrado
        content_frame = tk.Frame(main_frame, bg='#1e1e1e')
        content_frame.pack(expand=True)
        
        # Frame izquierdo para el sudoku
        left_frame = tk.Frame(content_frame, bg='#1e1e1e')
        left_frame.pack(side=tk.LEFT, padx=(0, 40))
        
        # Frame derecho para los botones
        right_frame = tk.Frame(content_frame, bg='#1e1e1e')
        right_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.create_sudoku_grid(left_frame)
        self.create_control_panel(right_frame)
        
    def create_sudoku_grid(self, parent):
        """Crear la cuadrícula del sudoku más grande"""
        # Frame para la cuadrícula con borde
        grid_frame = tk.Frame(parent, bg='#404040', bd=4, relief='solid')
        grid_frame.pack()
        
        self.entries = []
        
        for i in range(9):
            row_entries = []
            for j in range(9):
                # Determinar el color de fondo según la región 3x3
                bg_color = '#2a2a2a' if (i//3 + j//3) % 2 == 0 else '#353535'
                
                # Crear entry para cada celda - MUY aumentado
                entry = tk.Entry(grid_frame,
                               width=3,  # Más ancho
                               font=('Arial', 20, 'bold'),  # Fuente mucho más grande
                               justify='center',
                               bg=bg_color,
                               fg='white',
                               insertbackground='white',
                               bd=2,
                               relief='solid')
                
                # Configurar validación mejorada
                vcmd = (self.root.register(self.validate_input), '%P', '%W')
                entry.config(validate='key', validatecommand=vcmd)
                
                # Bind para verificar cuando cambie el valor con animación
                entry.bind('<KeyRelease>', lambda e, r=i, c=j, w=entry: self.on_value_change(r, c, w))
                entry.bind('<FocusOut>', lambda e, r=i, c=j, w=entry: self.on_focus_out(r, c, w))
                
                # Efectos hover para las celdas
                entry.bind('<Enter>', lambda e, w=entry: self.on_cell_hover_enter(w))
                entry.bind('<Leave>', lambda e, w=entry, bg=bg_color: self.on_cell_hover_leave(w, bg))
                
                # Posicionar entry con más espacio
                entry.grid(row=i, column=j, padx=2, pady=2, ipady=8)  # Mucho más grande
                row_entries.append(entry)
                
            self.entries.append(row_entries)
    
    def on_cell_hover_enter(self, entry):
        """Efecto hover al entrar en una celda"""
        entry.config(bg='#4a4a4a', bd=3)
    
    def on_cell_hover_leave(self, entry, original_bg):
        """Efecto hover al salir de una celda"""
        entry.config(bg=original_bg, bd=2)
    
    def create_control_panel(self, parent):
        """Crear panel de control con botones más grandes"""
        # Título del panel más grande
        panel_title = tk.Label(parent,
                              text="🎮 Opciones",
                              font=('Arial', 20, 'bold'),  # Mucho más grande
                              bg='#1e1e1e',
                              fg='#00ff88')
        panel_title.pack(pady=(0, 25))
        
        # Botón Resolver - más grande
        resolve_btn = ttk.Button(parent,
                               text="⚡ Resolver",
                               style='Modern.TButton',
                               command=self.resolver_sudoku,
                               width=18)  # Más ancho
        resolve_btn.pack(pady=12)
        
        # Botón Ejemplo Sudoku - más grande
        example_btn = ttk.Button(parent,
                               text="🎲 Ejemplo Sudoku",
                               style='Modern.TButton',
                               command=self.generar_ejemplo,
                               width=18)  # Más ancho
        example_btn.pack(pady=12)
        
        # Botón Limpiar - más grande
        clear_btn = ttk.Button(parent,
                             text="🧹 Limpiar",
                             style='Modern.TButton',
                             command=self.limpiar_sudoku,
                             width=18)  # Más ancho
        clear_btn.pack(pady=12)
        
        # Agregar indicador de dificultad aquí debajo de los botones
        self.create_difficulty_display(parent)
        
    def create_difficulty_display(self, parent):
        """Crear indicador de dificultad debajo de los botones"""
        # Frame para dificultad con espacio superior
        diff_frame = tk.Frame(parent, bg='#1e1e1e')
        diff_frame.pack(pady=(30, 0))
        
        # Container con fondo gris
        diff_container = tk.Frame(diff_frame, bg='#404040', bd=3, relief='solid')
        diff_container.pack()
        
        # Label de dificultad
        diff_label = tk.Label(diff_container,
                             text="🎯 Dificultad:",
                             font=('Arial', 16, 'bold'),  # Ajustado para el panel lateral
                             bg='#404040',
                             fg='#00ff88')
        diff_label.pack(padx=(15, 10), pady=12)
        
        # Entry para mostrar dificultad
        self.difficulty_entry = tk.Entry(diff_container,
                                       textvariable=self.dificultad_var,
                                       font=('Arial', 16, 'bold'),  # Ajustado
                                       width=12,
                                       justify='center',
                                       bg='#505050',
                                       fg='#00ff88',
                                       state='readonly',
                                       bd=2,
                                       relief='solid',
                                       insertbackground='#00ff88')
        self.difficulty_entry.pack(padx=(10, 15), pady=(0, 12))
    
    def validate_input(self, value, widget_name):
        """Validar entrada solo números 1-9 o vacío - sin 0 ni mayores a 9"""
        if value == "":
            return True
        # Solo permite dígitos del 1 al 9, no 0 ni números mayores a 9
        if value.isdigit() and len(value) == 1 and 1 <= int(value) <= 9:
            return True
        return False
    
    def animate_cell(self, entry):
        """Crear animación simple para la celda"""
        original_bg = entry.cget('bg')
        
        # Animación de flash verde
        entry.config(bg='#00ff44')
        self.root.after(150, lambda: entry.config(bg='#004422'))
        self.root.after(300, lambda: entry.config(bg=original_bg))
    
    def on_value_change(self, row, col, widget):
        """Manejar cambios en las celdas del sudoku con animación"""
        try:
            # Evitar verificaciones múltiples
            if self.verificando:
                return
                
            # Resetear flag de error cuando el usuario modifica algo
            self.error_mostrado = False
                
            # Animar la celda cuando se ingresa un valor
            value = widget.get()
            if value.isdigit():
                self.animate_cell(widget)
            
            # Actualizar matriz
            self.update_matrix_from_gui()
            
        except Exception as e:
            print(f"Error en cambio de valor: {e}")
    
    def on_focus_out(self, row, col, widget):
        """Verificar solo cuando se pierde el foco - CORREGIDO para evitar doble ventana"""
        try:
            # Evitar verificaciones múltiples y errores ya mostrados
            if self.verificando or self.error_mostrado:
                return
                
            self.verificando = True
            
            # Actualizar matriz
            self.update_matrix_from_gui()
            
            # Verificar sudoku solo si hay valores
            if np.any(self.sudoku_matrix != 0):
                if not verificacion(self.sudoku_matrix):
                    self.error_mostrado = True  # Marcar que ya se mostró error
                    # Usar after para evitar bloqueo
                    self.root.after(100, lambda: self.mostrar_error_verificacion())
            
            self.verificando = False
            
        except Exception as e:
            print(f"Error en verificación: {e}")
            self.verificando = False
    
    def mostrar_error_verificacion(self):
        """Mostrar error de verificación de forma controlada - UNA SOLA VEZ"""
        if not self.verificando and self.error_mostrado:
            messagebox.showerror("❌ Error", 
                               "Hay un error en el Sudoku.\nDebe modificarse.")
    
    def update_matrix_from_gui(self):
        """Actualizar la matriz numpy desde la GUI"""
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                self.sudoku_matrix[i][j] = int(value) if value.isdigit() else 0
    
    def update_gui_from_matrix(self, matrix):
        """Actualizar la GUI desde una matriz numpy con animación"""
        for i in range(9):
            for j in range(9):
                value = matrix[i][j]
                self.entries[i][j].delete(0, tk.END)
                if value != 0:
                    self.entries[i][j].insert(0, str(value))
                    # Animar las celdas que se llenan automáticamente
                    self.root.after(i * 50 + j * 10, lambda e=self.entries[i][j]: self.animate_cell(e))
    
    def resolver_sudoku(self):
        """Resolver el sudoku actual"""
        try:
            # Resetear flags de error
            self.error_mostrado = False
            
            # Actualizar matriz desde GUI
            self.update_matrix_from_gui()
            
            # Primero verificar si es válido
            if not verificacion(self.sudoku_matrix):
                messagebox.showerror("❌ Error", 
                                   "El Sudoku actual no es válido.\nCorrege los errores antes de resolver.")
                return
            
            # Resolver sudoku
            matriz_solucionada, dificultad = Resolver(self.sudoku_matrix)
            
            # Actualizar GUI con solución
            self.update_gui_from_matrix(matriz_solucionada)
            self.sudoku_matrix = matriz_solucionada.copy()
            
            # Actualizar dificultad
            self.dificultad_var.set(dificultad)
            
            messagebox.showinfo("✅ Éxito", "¡Sudoku resuelto correctamente!")
            
        except Exception as e:
            messagebox.showerror("❌ Error", f"Error al resolver: {str(e)}")
    
    def generar_ejemplo(self):
        """Generar un sudoku de ejemplo"""
        try:
            # Resetear flags de error
            self.error_mostrado = False
            
            # Generar sudoku
            matriz_generada, dificultad = generar_sudoku_jugable()
            
            # Actualizar GUI
            self.update_gui_from_matrix(matriz_generada)
            self.sudoku_matrix = matriz_generada.copy()
            
            # Actualizar dificultad
            self.dificultad_var.set(dificultad)
            
            messagebox.showinfo("🎲 Nuevo Sudoku", f"Sudoku generado con dificultad: {dificultad}")
            
        except Exception as e:
            messagebox.showerror("❌ Error", f"Error al generar: {str(e)}")
    
    def limpiar_sudoku(self):
        """Limpiar completamente el sudoku"""
        try:
            # Resetear flags de error
            self.error_mostrado = False
            
            # Limpiar todas las entradas
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
            
            # Resetear matriz
            self.sudoku_matrix = np.zeros((9, 9), dtype=int)
            
            # Resetear dificultad
            self.dificultad_var.set("Ninguna")
            
            messagebox.showinfo("🧹 Limpiado", "Sudoku limpiado correctamente")
            
        except Exception as e:
            messagebox.showerror("❌ Error", f"Error al limpiar: {str(e)}")

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
def main():
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()