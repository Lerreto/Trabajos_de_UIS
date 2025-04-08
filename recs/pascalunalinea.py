def pascal(n):return [1] if n==1 else [1,1] if n==2 else [1]+[sum(pascal(n-1)[i:i+2]) for i in range(n-2)]+[1]

for i in range(4, 8):
    print(pascal(i))
    
    
# 59689371400 -     19116299500
# 56004463300