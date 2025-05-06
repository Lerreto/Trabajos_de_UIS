"""

2.) Construir un programa que permita escoger entre dos operaciones, usando un
menú. La primera, leer un número n y determinar si es par o impar. La segunda,
leer un número n y determinar si es primo o no. n debe ser un número entero
positivo. El programa debe detectar si la opción escogida es o no válida.

"""

# Imprimo mas decorativamente
print("-" * 20 + " Punto 2 " + "-" * 20)

# Como lo voy a repetir mejor ahorar proceso
menu = """

    BIENVENIDOS AL MENU:

    Entre estas 2 opciones puedes hacer operaciones, escoge segun el numero

    ADVERTENCIA = Debe ser un numero entero positivo

    1.) Determina si el numero es par o impar
    2.) Determinar si el numero es primo o no
    3.) Volver a mostrar el menu
    4.) Esta opcion es para salir
"""

print(menu)

# Esto es para mantener al usuario dentro del menu
while True:
    
    # Pide el numero para poder ver que accion hacer
    n = input("\nIngrese la accion que quieres realizar = ")

    # n.isalpha sirve para verificar si hay caracteres en una cadena de texto, y la otra condicion para ver si n se encuentra en las opciones establecidas
    if not(n.isalpha()) and 1 <= int(n) <= 4:

        # En dado caso de ser asi lo convierte en un entero, porque al pedir el numero me lo da en str
        n = int(n)

        # Para salir del menu
        if n == 4:
            break
        
        # En dado caso que pida el menu
        elif n == 3:
            print(menu)

        # Determinar si es un numero primo o no
        elif n == 2:

            # Pide de nuevo el valor de n para hacer la accion
            n = int(input("\nIngrese el numero para hacer la accion = "))

            # Me facilita determinar si es primo o no, el primo va a ser a condicion, y el contador cuantos numeros son divisible con n
            primo, contador_divisible = True, 0
            
            # Verefico que sean mayor de 1
            if n > 1:
                # Verifico en cada numero si x es divisible con n
                for x in range(1, n+1):
                    # En dado de ser asi lo agrego al contador cada vez
                    if n % x == 0:
                        contador_divisible += 1
                    # Si el contador es mayor de 2 (porque 1 y el propio numero son divisibles) significa que no es primo y se sale del for para ahorrar proceso
                    if contador_divisible > 2:
                        primo = False
                        break
            else:
                primo = False
            
            # En dado caso de ser verdadero se imprime el mensaje correspondiente
            if primo:
                print(f"El numero {n} si es primo")
            else:
                print(f"El numero {n} no es primo")

        # En este no le pongo elif porque no hay necesidad, se sabe que esta entre el rango, por lo tanto solo queda una unica opcion, y es la operacion 1
        else:
            
            # Pido n nuevamente para verificar mas adelante si es par o impar
            n = int(input("\nIngrese el numero para hacer la accion = "))

            # Si el residuo es igual a 0 cuando se divide con 2 entonces es par
            if n % 2 == 0:
                print(f"El numero {n} es par")
            else:
                print(f"El numero {n} es impar")
    
    # En dado caso no ser un numero o estar por fuera del rango se imprime un error y el menu nuevamente
    else:
        print(f"ERROR: Recuerda cumplir con los parametros\n{menu}")


