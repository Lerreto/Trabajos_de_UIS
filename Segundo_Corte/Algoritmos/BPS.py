import matplotlib.pyplot as plt
import random

# Tamaño del mapa
WIDTH, HEIGHT = 100, 60
MIN_SIZE = 12

# Clase que representa un nodo de partición BSP
class Room:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.left = None
        self.right = None
        self.room = None  # Sub-área para una habitación

    def split(self):
        if self.left or self.right:
            return False  # Ya dividido

        horizontal = random.choice([True, False])
        if self.w > self.h and self.w / self.h >= 1.25:
            horizontal = False
        elif self.h > self.w and self.h / self.w >= 1.25:
            horizontal = True

        max_split = (self.h if horizontal else self.w) - MIN_SIZE
        if max_split <= MIN_SIZE:
            return False

        split = random.randint(MIN_SIZE, max_split)
        if horizontal:
            self.left = Room(self.x, self.y, self.w, split)
            self.right = Room(self.x, self.y + split, self.w, self.h - split)
        else:
            self.left = Room(self.x, self.y, split, self.h)
            self.right = Room(self.x + split, self.y, self.w - split, self.h)
        return True

    def get_leaf_rooms(self):
        if not self.left and not self.right:
            return [self]
        leaves = []
        if self.left:
            leaves += self.left.get_leaf_rooms()
        if self.right:
            leaves += self.right.get_leaf_rooms()
        return leaves

def create_bsp(root, depth):
    if depth <= 0:
        return
    if root.split():
        create_bsp(root.left, depth - 1)
        create_bsp(root.right, depth - 1)

# Crear raíz y dividir
root = Room(0, 0, WIDTH, HEIGHT)
create_bsp(root, 5)

# Visualizar divisiones BSP
fig, ax = plt.subplots(figsize=(12, 8))
def draw_room(room):
    rect = plt.Rectangle((room.x, room.y), room.w, room.h, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    if room.left: draw_room(room.left)
    if room.right: draw_room(room.right)

draw_room(root)
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')
ax.invert_yaxis()
plt.title("División de espacio con BSP")
plt.show()