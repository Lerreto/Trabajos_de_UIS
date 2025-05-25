import tkinter as tk
def checker(valor):
    if valor == "":
        return True
    return valor == "" or (valor.isdigit() and 1 <= int(valor) <= 9)

def resolver():
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
    print(sudoku)
def reiniciar():
    ventana.destroy()
    main()
def main():
    global ventana, sudokutemp
    ventana = tk.Tk()

    ventana.title("Sudokapp") #El nombre uwu
    ventana.geometry('640x480')
    ventana.resizable(False, False)

    vf = ventana.register(checker)
    tablero_frame = tk.Frame(ventana) #Es un contenedor
    tablero_frame.pack(pady=10)#Se le agregan 20px de espacio arriba y abajo
    sudokutemp = [] #Matriz del sudoku
    for row in range(9):
        filasu = []#Lista de cada fila
        for col in range(9):
            if row % 3 == 0:#Detalles esteticos para los bordes del sudoku
                top_bor = 5
            else: 
                top_bor = 1
            if col % 3 == 0:
                left_bor = 5
            else: 
                left_bor = 1
            caja = tk.Entry(   
                tablero_frame, 
                width = 2, 
                relief ="solid",
                font=('Arial', 18),
                validate = "key",
                bd = 1,
                validatecommand=(vf, "%P")
                )
            
            caja.grid(row=row, column= col, padx = (left_bor,0), pady=(top_bor, 0))
            filasu.append(caja)
            
        sudokutemp.append(filasu)
        
    boton_resolver = tk.Button( ventana, text="Resolver", bd = 3, command=resolver)
    boton_reiniciar = tk.Button( ventana, text="Reiniciar", bd = 3, command=reiniciar)

    boton_resolver.place(x=180, y=400)
    boton_reiniciar.place(x=320, y=400)

    #VARIABLE QUE NOS DA LA MATRIZ = sudoku
    ventana.mainloop()
main()