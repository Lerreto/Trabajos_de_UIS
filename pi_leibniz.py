n = int(input())
suma = 0
for i in range(0, n + 1, 1):
    suma = suma + -1 ** i / 2 * i + 1
print(suma * 4)
