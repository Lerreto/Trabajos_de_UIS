"""

1. Construir un programa que permita cifrar y descifrar una frase usando el cifrado conocido coloquialmentecomo el cifrado de César. Este cifrado consiste en reemplazar cada letra de un texto por la letra que está tres posiciones adelante en el alfabeto, por ejemplo cambiar todas las “A” por “D”; este valor de tres, para tres posiciones del alfabeto, lo llamaremos valor de salto, y puede variar. Este programa debe hacer algo más: usar el valor de salto de 3 para las palabras en posiciones pares y el valor de salto de 4 para las que estén en posiciones impares. El programa naturalmente tomará los espacios en blanco como separador de palabras y los ignorará para el proceso de reemplazo, al igual que los signos de puntuación.
    
"""

frase = str(input("Ingrese un texto para poder hacer el cifrado: "))

def cifrado_cesar(texto):
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cadena_vacia = ""
    
    for x, i in enumerate(texto.lower()):
        if i in abecedario:
            if (x + 1) % 2 == 0:
                salto = 3
            else:
                salto = 4
        
            new_posicion = (abecedario.index(i) + salto) % 27
            new_letra = abecedario[new_posicion]
            
        else:
            new_letra = i
        
        cadena_vacia += new_letra
        
    return f"La cadena con el cifrado Cesar es = {cadena_vacia}"

imprimir = cifrado_cesar(frase)
print(imprimir)