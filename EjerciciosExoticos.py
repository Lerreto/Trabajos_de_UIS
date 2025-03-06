# Ejercicios exoticos para fundamentos de programacion

"""
1.) Convierta un numero dado por el usuario (N) en su representacion en base b (2 <= b < 10). = def baseN()

2.) Escriba una lista de numeros de 0 hasta n, cuando sean divisibles por 2, 3 0 5. = def writeList()

3.) Separa las palabras de una frase dada por el usuario, por los espacios. = def separacion() 

4.) presente un menu con las operaciones aritmeticas (+, -, *, /) y haga la operacion seleccionada. debe repetir el proceso hasta que se escoja la opcion salir. = def menu()

5.) Convierta una palabra a Pig Latin. = def pigLatin()
"""
# Lo voy a separar por medio de funciones

# EJERCICIO 1.)

def baseN():
    print(f"\n{"-"*20} Ejercicio 1 {"-"*20}")
    
    b, n, base = 0, 0, ""
    while (2 > b) or (b > 10): 
        print("\nREGLAS:\n1.)Rango admitido: (2 <= b < 10)\n2.)Tipo de dato: Entero\n")
        b = int(input("Ingresa la base del numero que quieres hacer = "))
        
    n = int(input(f"\nNumero n a pasar a base {b} = "))
    
    while n != 0:
        residuo = n % b
        n = n // b
        base = str(residuo) + base

    return f"\n El numero {n} en base {b} es: {base}"

dato = baseN()
print(dato)

# EJERCICIO 2.)

def writeList():
    print(f"\n{"-"*20} Ejercicio 2 {"-"*20}")
    
    n, lista = 0, []
    while n < 2:
        print("\nREGLAS:\n1.) N debe de ser mayor a 2\n2.) Se va a ser una lista hasta n cuando sean divisibles por 2,3 o 5\n")
        
        n = int(input("Ingerese n para hacer la lista correspondiente = ")) 
        
    for x in range(1, n + 1):
        if any(x % n == 0 for n in [2, 3, 5]):
            lista.append(x)
    
    return lista

dato = writeList()
print(dato)            
 
 
# Ejercicio 3.)

def separacion():
    print(f"\n{"-"*20} Ejercicio 3 {"-"*20}")
    
    frase, palabra = "", ""
    
    while not(" " in frase):
        print("\nREGLAS:\n1.) Debe de ser una frase\n2.) Debe de ser un string\n")
        frase = str(input("Ingrese la frase para poder separarla = "))
        
    for letra in frase:
        if letra == " ":
            print(palabra)
            palabra = ""
        else:
            palabra += letra
    print(palabra)
    
separacion()    
   
        
# Ejercicio 4.)

def menu():
    print(f"\n{"-"*20} Ejercicio 4 {"-"*20}")
    
    menu = ("""
              
    REGLAS DEL MENU:
              
    1.) Para poder salir escribir: salir
    2.) Va a servir para operaciones aritmeticas basicas entre 2 valores
    3.) Las opciones son: | + | - | * | / |
    4.) Si quieres otra vez las reglas escribe: menu
              
              """)
    
    string = ""
    print(menu)
    while string != "salir":
        n = str(input("\nQue deseas hacer en este menu exotico? = " ))
        string = n.lower()
        
        if string in ["+", "-", "*", "/", "menu"]:
        
            if string == "menu":
                print(menu)
                
            elif string in ["+", "-", "*", "/"]:
                a, b = "", ""
                while not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                    print("Debe de ser un número entero o float ambos.")
            
                    # Verificar si a y b son números válidos antes de continuar
                    try:
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        
                    except ValueError:
                        
                        print("\nPor favor, ingresa valores válidos (números).\n")
                        a, b = "", ""  # Reiniciar a y b si la entrada no es válida
                    
            if string == "+":
                print(f"La suma de {a} y {b} es: {a + b:.2f}")  # Realiza la suma de a y b
            elif string == "-":
                print(f"La resta de {a} y {b} es: {a - b:.2f}")  # Realiza la resta de a y b
            elif string == "/":
                if b != 0:  # Asegura que no haya división por cero
                    print(f"La división de {a} entre {b} es: {a / b:.2f}")  # Realiza la división de a entre b
                else:
                    print("Error: No se puede dividir por cero.")  # Mensaje de error por división por cero
            elif string == "*":
                print(f"La multiplicación de {a} y {b} es: {a * b:.2f}")  # Realiza la multiplicación de a y b
                
        else:
            print("Ingrese una de las opciones validas")
            
menu()