"""

1. Construir un programa que permita cifrar y descifrar una frase usando el cifrado conocido coloquialmentecomo el cifrado de César. Este cifrado consiste en reemplazar cada letra de un texto por la letra que está tres posiciones adelante en el alfabeto, por ejemplo cambiar todas las “A” por “D”; este valor de tres, para tres posiciones del alfabeto, lo llamaremos valor de salto, y puede variar. Este programa debe hacer algo más: usar el valor de salto de 3 para las palabras en posiciones pares y el valor de salto de 4 para las que estén en posiciones impares. El programa naturalmente tomará los espacios en blanco como separador de palabras y los ignorará para el proceso de reemplazo, al igual que los signos de puntuación.
    
"""
import string

def cifrado_cesar(accion, texto):
    cadena_vacia = ""
    accion.lower()
    
    for x, i in enumerate(texto):
        if i.isalpha():
            alfabeto = string.ascii_uppercase if i.isupper() else string.ascii_lowercase
            salto = 4 if (x + 1) % 2 == 0 else 3
            actual_pos = alfabeto.index(i)
            if accion == "cifrar":
                new_pos = (actual_pos + salto) % 26
            else:
                new_pos = (actual_pos - salto) % 26
            new_letter = alfabeto[new_pos]
        else:
            new_letter = i
        cadena_vacia += new_letter
        
    return f"""Texto original = - {texto} -
Texto {accion} = - {cadena_vacia} -"""    
        
imprimir = cifrado_cesar("descifrar", "Ksoe! tyh weo? szs")
imprimir2 = cifrado_cesar("cifrar", "Hola! que tal? owo")
print(imprimir)
print(imprimir2)
                
  
    
   


