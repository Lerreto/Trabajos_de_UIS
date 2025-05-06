a = int(input())
b = int(input())
c = int(input())
if a > b:
    if b > c:
        print("A > B > C")
        print(str(a) + " > " + str(b) + " > " + str(c))
    else:
        if c > a:
            print("C > A > B")
            print(str(c) + " > " + str(a) + " > " + str(b))
        else:
            print("A > C > B")
            print(str(a) + " > " + str(c) + " > " + str(b))
else:
    if a > c:
        print("B > A > C")
        print(str(b) + " > " + str(a) + " > " + str(c))
    else:
        if c > b:
            print("C > B > A")
            print(str(c) + " > " + str(b) + " > " + str(a))
        else:
            print("B > C > A")
            print(str(b) + " > " + str(c) + " > " + str(a))
