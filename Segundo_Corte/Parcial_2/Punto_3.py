"""

3. Construir un programa que lea una frase cualquiera y convierta la
primera letra de cada palabra en mayúscula (la función upper()
convierte una cadena cualquiera en mayúscula); esta conversión debe
realizarse mediante una función escrita por ustedes mismos que reciba
una palabra y devuelva la misma palabra con la letra inicial en
mayúscula.

"""
# En este apartado me ingresa la frase
frase = input("Ingrese la frase que desees = ")

# Es la funcion donde se va a ejecutar el programa
def mayusculas_palabras(n):
    # Dividir la frase en una lista tomando de referencia los espacios
    separado = frase.split(" ")
    mayusculas = []
    
    # Crea una nueva palabra donde la primera letra es mayuscula, y luego se le suma el resto de la palabra en adelante
    for i in separado:
        nueva_palabra = i[0].upper() + i[1:]
        mayusculas.append(nueva_palabra)
        
    # Esta es una manera reducida, pero pues no la pongo pq no lo hemos visto
    #mayusculas = list(map(str.capitalize, separado))

    # Es una funcion de join que lo que hace es contatenar, el " " dice como es que se va a dividir, y el join se le pone de la lista
    new_list = " ".join(mayusculas)
    print(new_list)

# Imprimo la frase modificada
mayusculas_palabras(frase)