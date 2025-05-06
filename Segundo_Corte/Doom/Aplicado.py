# https://www.canva.com/design/DAGlTHcDsU8/G3NEDss_78ZPlycBh9btAg/edit?utm_content=DAGlTHcDsU8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
import numpy as np
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = None
        self.right = None
        self.room = None
        
    def split(self, min_size=3):
        # Si no es lo suficientemente grande para dividir
        if self.width < min_size*2 or self.height < min_size*2:
            return False
            
        # Decidir si dividir horizontal o verticalmente
        horizontal = random.choice([True, False])
        if self.width > self.height * 1.25:  # Mucho más ancho que alto
            horizontal = False
        elif self.height > self.width * 1.25:  # Mucho más alto que ancho
            horizontal = True
            
        # Encontrar dónde dividir
        if horizontal:
            split_pos = random.randint(min_size, self.height - min_size)
            # Crear nodos hijos
            self.left = Node(self.x, self.y, self.width, split_pos)
            self.right = Node(self.x, self.y + split_pos, self.width, self.height - split_pos)
        else:
            split_pos = random.randint(min_size, self.width - min_size)
            # Crear nodos hijos
            self.left = Node(self.x, self.y, split_pos, self.height)
            self.right = Node(self.x + split_pos, self.y, self.width - split_pos, self.height)
            
        return True
        
    def create_room(self):
        # Si tiene hijos, no crear habitación aquí
        if self.left or self.right:
            return
            
        # Crear una habitación de tamaño aleatorio dentro del nodo
        room_width = random.randint(3, self.width - 2)
        room_height = random.randint(3, self.height - 2)
        
        # Posición aleatoria dentro del nodo
        room_x = self.x + random.randint(1, self.width - room_width - 1)
        room_y = self.y + random.randint(1, self.height - room_height - 1)
        
        # Guardar la habitación como (x, y, ancho, alto)
        self.room = (room_x, room_y, room_width, room_height)
        
    def get_rooms(self):
        rooms = []
        if self.room:
            rooms.append(self.room)
        if self.left:
            rooms.extend(self.left.get_rooms())
        if self.right:
            rooms.extend(self.right.get_rooms())
        return rooms
        
    def get_leaf_nodes(self):
        if not self.left and not self.right:
            return [self]
        nodes = []
        if self.left:
            nodes.extend(self.left.get_leaf_nodes())
        if self.right:
            nodes.extend(self.right.get_leaf_nodes())
        return nodes

# Función principal para generar la mazmorra
def generate_dungeon(width, height, max_splits=4):
    # Crear mapa inicial (1=pared, 0=espacio vacío)
    dungeon = np.ones((height, width), dtype=int)
    
    # Crear nodo raíz
    root = Node(0, 0, width, height)
    
    # Lista para llevar el seguimiento de los nodos a dividir
    nodes = [root]
    
    # Hacer divisiones según max_splits
    splits = 0
    while splits < max_splits and nodes:
        current_node = nodes.pop(0)
        if current_node.split():
            nodes.append(current_node.left)
            nodes.append(current_node.right)
            splits += 1
    
    # Obtener todos los nodos hoja (donde irán las habitaciones)
    leaf_nodes = root.get_leaf_nodes()
    
    # Crear habitaciones en cada nodo hoja
    for node in leaf_nodes:
        node.create_room()
    
    # Dibujar habitaciones en el mapa
    rooms = root.get_rooms()
    for room in rooms:
        x, y, w, h = room
        dungeon[y:y+h, x:x+w] = 0  # 0 = espacio vacío
    
    # Conectar habitaciones con pasillos
    for i in range(len(rooms) - 1):
        # Conectar centro de una habitación con centro de la siguiente
        x1 = rooms[i][0] + rooms[i][2] // 2
        y1 = rooms[i][1] + rooms[i][3] // 2
        x2 = rooms[i+1][0] + rooms[i+1][2] // 2
        y2 = rooms[i+1][1] + rooms[i+1][3] // 2
        
        # Trazar un pasillo en forma de L
        # Primero horizontal, luego vertical
        for x in range(min(x1, x2), max(x1, x2) + 1):
            dungeon[y1, x] = 0
        for y in range(min(y1, y2), max(y1, y2) + 1):
            dungeon[y, x2] = 0
    
    return dungeon, rooms

# Visualización del mapa
def show_dungeon(dungeon, rooms=None):
    plt.figure(figsize=(8, 6))
    plt.imshow(dungeon, cmap='binary', interpolation='none')
    
    # Resaltar las habitaciones
    if rooms:
        for room in rooms:
            x, y, w, h = room
            plt.gca().add_patch(plt.Rectangle((x-0.5, y-0.5), w, h, 
                               fill=False, edgecolor='blue', linewidth=1))
    
    plt.title("Mazmorra generada con BSP")
    plt.tight_layout()
    plt.show()

# Ejecutar la generación
if __name__ == "__main__":
    width, height = 40, 30
    dungeon, rooms = generate_dungeon(width, height, max_splits=5)
    show_dungeon(dungeon, rooms)