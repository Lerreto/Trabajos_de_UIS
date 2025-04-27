"""
    
5. Construir un programa que reciba las componentes en x y y de un vector y calcule una proyección del mismo sobre un par de vectores unitarios al azar. El programa de permitir recibir más de un vector, pero uno a la vez. Para cada caso graficar el punto inicial y los puntos que representan las proyecciones.
    
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def generar_vectores_unitarios(cantidad=2):
    """Genera vectores unitarios aleatorios"""
    vectores = []
    for _ in range(cantidad):
        # Generar componentes aleatorias
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        # Normalizar para que sea unitario
        magnitud = np.sqrt(x**2 + y**2)
        vectores.append((x/magnitud, y/magnitud))
    
    return vectores

def calcular_proyeccion(vector, vector_unitario):
    """Calcula la proyección de un vector sobre un vector unitario"""
    # El producto punto da la magnitud de la proyección
    magnitud_proyeccion = vector[0] * vector_unitario[0] + vector[1] * vector_unitario[1]
    
    # Las componentes de la proyección son el vector unitario escalado por la magnitud
    proyeccion = (magnitud_proyeccion * vector_unitario[0], 
                  magnitud_proyeccion * vector_unitario[1])
    
    return proyeccion

def graficar_vector_y_proyecciones(vector, proyecciones, vectores_unitarios):
    """Grafica el vector original y sus proyecciones"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Determinamos los límites del gráfico basados en los vectores
    todos_puntos = [vector] + proyecciones
    max_coord = max([max(abs(p[0]), abs(p[1])) for p in todos_puntos]) * 1.2
    
    # Configurar el gráfico
    ax.set_xlim(-max_coord, max_coord)
    ax.set_ylim(-max_coord, max_coord)
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax.set_aspect('equal')
    
    # Dibujar el vector original (rojo)
    arrow_orig = FancyArrowPatch((0, 0), vector, 
                                 arrowstyle='->', 
                                 mutation_scale=15, 
                                 color='red', 
                                 linewidth=2)
    ax.add_patch(arrow_orig)
    
    # Dibujar los vectores unitarios (negro)
    for i, v_unit in enumerate(vectores_unitarios):
        # Escalamos para visualización
        v_scaled = (v_unit[0] * max_coord * 0.4, v_unit[1] * max_coord * 0.4)
        arrow_unit = FancyArrowPatch((0, 0), v_scaled, 
                                     arrowstyle='->', 
                                     mutation_scale=15, 
                                     color='black', 
                                     linewidth=1, 
                                     alpha=0.7)
        ax.add_patch(arrow_unit)
        ax.text(v_scaled[0] * 1.1, v_scaled[1] * 1.1, f'u{i+1}', fontsize=12)
    
    # Dibujar las proyecciones (azul)
    for i, proy in enumerate(proyecciones):
        arrow_proy = FancyArrowPatch((0, 0), proy, 
                                     arrowstyle='->', 
                                     mutation_scale=15, 
                                     color='blue', 
                                     linewidth=2, 
                                     linestyle='--')
        ax.add_patch(arrow_proy)
        ax.text(proy[0] * 1.1, proy[1] * 1.1, f'Proy_{i+1}', fontsize=10)
    
    # Añadir texto con coordenadas
    ax.plot(vector[0], vector[1], 'ro')
    ax.text(vector[0] * 1.05, vector[1] * 1.05, f'Vector ({vector[0]:.2f}, {vector[1]:.2f})', fontsize=10)
    
    for i, proy in enumerate(proyecciones):
        ax.plot(proy[0], proy[1], 'bo')
        ax.text(proy[0] * 1.05, proy[1] * 1.05, f'Proy_{i+1} ({proy[0]:.2f}, {proy[1]:.2f})', fontsize=8)
    
    ax.set_title(f'Vector ({vector[0]:.2f}, {vector[1]:.2f}) y sus proyecciones')
    ax.set_xlabel('Componente X')
    ax.set_ylabel('Componente Y')
    
    # Añadir leyenda
    plt.plot([], [], 'r-', label='Vector original')
    plt.plot([], [], 'k-', label='Vectores unitarios')
    plt.plot([], [], 'b--', label='Proyecciones')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    print("Calculadora de Proyecciones de Vectores")
    print("---------------------------------------")
    
    continuar = True
    
    while continuar:
        # Solicitar componentes del vector
        try:
            x = float(input("Ingrese la componente X del vector: "))
            y = float(input("Ingrese la componente Y del vector: "))
            vector = (x, y)
            
            # Generar vectores unitarios aleatorios
            num_vectores = 2  # Por defecto generamos 2 vectores unitarios
            vectores_unitarios = generar_vectores_unitarios(num_vectores)
            
            # Calcular proyecciones
            proyecciones = []
            for i, v_unit in enumerate(vectores_unitarios):
                proyeccion = calcular_proyeccion(vector, v_unit)
                proyecciones.append(proyeccion)
                print(f"Proyección sobre u{i+1} {v_unit}: ({proyeccion[0]:.4f}, {proyeccion[1]:.4f})")
            
            # Graficar
            graficar_vector_y_proyecciones(vector, proyecciones, vectores_unitarios)
            
            # Preguntar si se desea continuar
            respuesta = input("¿Desea ingresar otro vector? (s/n): ").lower()
            continuar = respuesta == 's' or respuesta == 'si'
            
        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()