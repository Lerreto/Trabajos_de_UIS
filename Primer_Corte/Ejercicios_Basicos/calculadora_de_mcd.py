n1 = int(input())
n2 = int(input())
if n1 < n2:
    for i in range(1, n1 + 1, 1):
        if n1 % i == 0 and n2 % i == 0:
            mcd = i
else:
    if n1 > n2:
        i = 1
        while i <= n2:
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
            i = i + 1
    else:
        mcd = n1
print(mcd)
