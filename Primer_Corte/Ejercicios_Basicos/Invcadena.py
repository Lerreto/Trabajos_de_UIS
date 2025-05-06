entrada = str(input("Ingrese la cadena que quiere invertir = "))
n = len(entrada)
salida = ""

for i in range(n):
    print(entrada[i])
    salida = entrada[i] + salida
    print(salida)

print("La cadena invertida es: " + salida)