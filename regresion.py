import random as ran
import matplotlib.pyplot as plt
import numpy as np

n = 10
puntos = []

for x in range(n):
    x = ran.randint(1, 6)
    y = ran.randint(10, 100)
    puntos.append([x, y])
    
print(puntos)

suma_x = 0
suma_y = 0
suma_xy = 0
suma_x2 = 0


for i in puntos:
    x = i[0]
    y = i[1]
    print(i)
    suma_x += x
    suma_y += y
    suma_xy += (x*y)
    suma_x2 += (x**2)
    
a = ((n*suma_xy - suma_x*suma_y) / (n*suma_x2 - suma_x**2))
b = ((suma_y - a*suma_x) / (n))

x2 = []
y2 = []

print(f"y = {a}x + {b}")

plt.plot(a, b, "g-")
plt.show()


x_vals = [p[0] for p in puntos]
y_vals = [p[1] for p in puntos]

plt.scatter(x_vals, y_vals, color="blue", label="Puntos generados")

# Graficar la línea de regresión
x_line = np.linspace(min(x_vals), max(x_vals), 100)
y_line = a * x_line + b
plt.plot(x_line, y_line, color="red", label=f"Regresión: y = {a:.2f}x + {b:.2f}")

# Personalización del gráfico
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico de puntos y línea de regresión")
plt.legend()

# Mostrar el gráfico
plt.show()