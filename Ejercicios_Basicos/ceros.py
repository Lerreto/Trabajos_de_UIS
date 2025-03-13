n = int(input("Introduzca n: "))
nback = n
m = 0
factor = 0
while n > 0:
    r = n % 10
    n = n // 10
    m = r * factor + m
    factor = factor * 100

print(str(m) + " -> " + str(nback))
print(f"{nback} - > {m}")
print("{} -> {}".format(m, nback))