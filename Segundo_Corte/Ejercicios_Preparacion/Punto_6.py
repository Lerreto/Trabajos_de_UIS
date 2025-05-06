import numpy as np

def evaluar_polinomio(coeficientes, x):
    """Evalúa el polinomio dado en el punto x."""
    return sum(coef * x ** (len(coeficientes) - i - 1) for i, coef in enumerate(coeficientes))

def suma_riemann(coeficientes, divisiones):
    """Calcula la suma de Riemann usando arrays para Caín y Abel."""
    # Inicializar arrays para las áreas
    areas_cain = np.zeros(divisiones)
    areas_abel = np.zeros(divisiones)
    
    for i in range(divisiones):
        xi = i / divisiones  # Calcular el punto xi
        valor_f = evaluar_polinomio(coeficientes, xi)
        
        # Ajustar el valor de la función para que esté en el rango [0, 1]
        if valor_f < 0:
            valor_f = 0  # No se suma nada a Caín
        elif valor_f > 1:
            valor_f = 1  # Caín solo recibe el valor 1
        
        # Almacenar el área de cada rectángulo en los arrays
        areas_cain[i] = valor_f / divisiones  # Añadir a Caín (parte inferior)
        areas_abel[i] = (1 - valor_f) / divisiones  # Añadir a Abel (parte superior)
    
    return areas_cain, areas_abel

def resolver_caso(grado, coeficientes, divisiones):
    """Resuelve el caso para un polinomio dado, dividiendo el terreno."""
    areas_cain, areas_abel = suma_riemann(coeficientes, divisiones)
    
    # Calcular las áreas totales para Caín y Abel
    suma_cain = np.sum(areas_cain)
    suma_abel = np.sum(areas_abel)
    
    # Calcular la diferencia y decidir el reparto
    diferencia = abs(suma_cain - suma_abel)
    
    if diferencia <= 0.001:
        return "JUSTO"
    elif suma_cain > suma_abel:
        return "CAIN"
    else:
        return "ABEL"

# Lectura de la entrada
while True:
    grado = int(input())
    if grado == 20:  # Fin de la entrada
        break
    
    coeficientes = list(map(int, input().split()))
    divisiones = int(input())
    
    # Resolver el caso actual
    resultado = resolver_caso(grado, coeficientes, divisiones)
    print(resultado)