def mcd(a, b):
    if a == 0 or b == 0 :
        return 0
    if a == b :
        return a
    if a > b :
        return mcd(a - b, b)
    elif b > a :
        return mcd(a, b-a)
    

A = int(input("Valor de a: "))
B = int(input("Valor de b: "))
print(mcd(A, B))