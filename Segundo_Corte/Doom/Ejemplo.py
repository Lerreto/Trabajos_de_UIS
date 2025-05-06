import matplotlib.pyplot as plt
import random
import numpy as np

def simple_bsp(x, y, width, height, depth=0, max_depth=3):
    """
    Función sencilla de partición binaria del espacio
    
    Parámetros:
    - x, y: coordenadas de la esquina superior izquierda del rectángulo
    - width, height: ancho y alto del rectángulo
    - depth: profundidad actual en el árbol
    - max_depth: profundidad máxima para detenerse
    
    Retorna:
    - Lista de rectángulos (cada uno como [x, y, width, height])
    """
    # Si alcanzamos la profundidad máxima, devolvemos este rectángulo
    if depth >= max_depth:
        return [[x, y, width, height]]
    
    rectangles = []
    
    # Decidir si dividir horizontal o verticalmente
    if width > height:
        # Dividir verticalmente (por x)
        split_pos = random.randint(int(width * 0.3), int(width * 0.7))
        
        # Llamada recursiva para división izquierda
        left_rects = simple_bsp(x, y, split_pos, height, depth + 1, max_depth)
        rectangles.extend(left_rects)
        
        # Llamada recursiva para división derecha
        right_rects = simple_bsp(x + split_pos, y, width - split_pos, height, depth + 1, max_depth)
        rectangles.extend(right_rects)
    else:
        # Dividir horizontalmente (por y)
        split_pos = random.randint(int(height * 0.3), int(height * 0.7))
        
        # Llamada recursiva para división superior
        top_rects = simple_bsp(x, y, width, split_pos, depth + 1, max_depth)
        rectangles.extend(top_rects)
        
        # Llamada recursiva para división inferior
        bottom_rects = simple_bsp(x, y + split_pos, width, height - split_pos, depth + 1, max_depth)
        rectangles.extend(bottom_rects)
    
    return rectangles

# Crear una figura para visualizar
plt.figure(figsize=(8, 8))
ax = plt.gca()

# Tamaño del plano total
plano_width = 100
plano_height = 100

# Aplicar BSP al plano
rectangulos = simple_bsp(0, 0, plano_width, plano_height, max_depth=3)

# Imprimir información sobre los fragmentos
print(f"Se generaron {len(rectangulos)} fragmentos:")
for i, (x, y, w, h) in enumerate(rectangulos):
    print(f"Fragmento {i+1}: Posición=({x},{y}), Tamaño={w}x{h}")

# Generar colores aleatorios para cada fragmento
colores = np.random.rand(len(rectangulos), 3)

# Dibujar cada rectángulo con un color aleatorio
for i, (x, y, w, h) in enumerate(rectangulos):
    color = colores[i]
    ax.add_patch(plt.Rectangle((x, y), w, h, fill=True, color=color, alpha=0.5))
    ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, edgecolor='black'))
    
    # Añadir texto con el número del fragmento
    plt.text(x + w/2, y + h/2, f"{i+1}", ha='center', va='center', fontsize=12)

# Configurar los límites y etiquetas
plt.xlim(0, plano_width)
plt.ylim(0, plano_height)
plt.title(f"Partición Binaria del Espacio (BSP) - {len(rectangulos)} fragmentos")
plt.xlabel("X")
plt.ylabel("Y")

# Mostrar la gráfica
plt.tight_layout()
plt.show()
