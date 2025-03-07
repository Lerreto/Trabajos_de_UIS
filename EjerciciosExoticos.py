# Ejercicios exoticos para fundamentos de programacion

"""
1.) Convierta un numero dado por el usuario (N) en su representacion en base b (2 <= b < 10). = def baseN()

2.) Escriba una lista de numeros de 0 hasta n, cuando sean divisibles por 2, 3 0 5. = def writeList()

3.) Separa las palabras de una frase dada por el usuario, por los espacios. = def separacion() 

4.) presente un menu con las operaciones aritmeticas (+, -, *, /) y haga la operacion seleccionada. debe repetir el proceso hasta que se escoja la opcion salir. = def menu()

5.) Convierta una palabra a Pig Latin. = def pigLatin()
"""
# Lo voy a separar por medio de funciones los diferentes ejercicios

# EJERCICIO 1

def baseN():
    # Imprimo el texto con un color para sobre salir
    print(f"\n\033[91m{"-"*20} Ejercicio 1 {"-"*20}\033[0m")
    
    # En este apartado declaro las variables
    b, n, base = 0, 0, ""
    # Deben de cumplir con los parametros o si no no salen para la base
    while (2 > b) or (b > 10): 
        print("""\033[92m
        REGLAS:
        
        1.)Rango admitido: (2 <= b < 10)
        2.)Tipo de dato: Entero
        
        \033[0m""")
        b = int(input("Ingresa la base del numero que quieres hacer = "))
        
    # Ahora pido el numero para transformarlo a esa base
    n = int(input(f"\nNumero n a pasar a base {b} = "))
    
    # De esta manera logro sacar el numero con la base correspondiente
    while n != 0:
        residuo = n % b
        n = n // b
        base = str(residuo) + base

    return f"\n El numero {n} en base {b} es: {base}"

# Aqui imprimo los datos
dato = baseN()
print(dato)



# EJERCICIO 2.)

def writeList():
    print(f"\n\033[91m{"-"*20} Ejercicio 2 {"-"*20}\033[0m")
    
    # Los numeros los voy a guardar en una lista
    n, lista = 0, []
    # El numero q debe de ingresar debe de ser mayor a 2
    while n < 2:
        print("""\033[92m
              
        REGLAS:
        
        1.) N debe de ser mayor a 2
        2.) Se va a ser una lista hasta n cuando sean divisibles por 2,3 o 5
        
        \033[0m""")
        
        n = int(input("Ingerese n para hacer la lista correspondiente = ")) 
        
    # Solo agrego aquellos que sean divisibles con 2, 3 y 5, por medio de una funcion any, la cual verica que se cumpla al menos una condicion con los diferentes numeros divisible
    for x in range(1, n + 1):
        if any(x % n == 0 for n in [2, 3, 5]):
            # En dado caso que sean divisible se agrega a la lista
            lista.append(x)
    
    return lista

dato = writeList()
print(dato)            
 
 
# Ejercicio 3.)

def separacion():
    print(f"\n\033[91m{"-"*20} Ejercicio 3 {"-"*20}\033[0m")
    
    frase, palabra = "", ""
    
    # Me verifica que no sea una sola palabra si no que una frase con el espacio
    while not(" " in frase):
        print("""\033[92m
              
        REGLAS:
        
        1.) Debe de ser una frase
        2.) Debe de ser un string
        
        \033[0m""")
        frase = str(input("Ingrese la frase para poder separarla = "))
        
    # Hago el proceso debido
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
    print(f"\n\033[91m{"-"*20} Ejercicio 4 {"-"*20}\033[0m")
    
    menu = ("""\033[92m
              
    REGLAS DEL MENU:
              
    1.) Para poder salir escribir: salir
    2.) Va a servir para operaciones aritmeticas basicas entre 2 valores
    3.) Las opciones son: | + | - | * | / |
    4.) Si quieres otra vez las reglas escribe: menu
              
    \033[0m""")
    
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
                # el isinstance verifica que el primer parametro pertenezca a uno de los tipos que le estoy pidiendo, de tal manera verifico que sean numeros
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

# Ejercicio 5.)

def pigLatin():
    print(f"\n\033[91m{"-"*20} Ejercicio 5 {"-"*20}\033[0m")
    print("""\033[92m
      
    REGLAS:
    
    1.) Este es el juego Pit Latin
    2.) Debes de ingresar una palabra, no un numero o frase
    3.) La palabra debe de ser de mas de 1 caracter    
    \033[0m""")
    
    salir = True
    
    # Verifico que sea una palabra de mas de 2 caracteres
    while salir:
        print("\n\033[93mADVERTENCIA = Debe de ser una palabra y en formato de string sin numeros\033[0m")
        palabra = input("Ingresa porfavor una palabra = ")
        if palabra.isalpha() and " " not in palabra and len(palabra) >= 2 :
            salir = False
    palabra = palabra.lower()
    
    return f'\nLa palabra quedaria como = {palabra[1:]}{palabra[0]}ay'
    
date = pigLatin()
print(date)
            