from time import perf_counter_ns

def pascal(n):
    if n==1:
        return [1]
    
    if n==2:
        return [1,1]
    
    previous = pascal(n-1)
    output = []
    
    for i in range(len(previous)-1):
        left = previous[i]
        right = previous[i+1]
        output.append(left + right)
    return [1] + output + [1]

antes = perf_counter_ns()
for i in range(1, 1001):
    #print(pascal(i))
    pascal(i)
despues = perf_counter_ns()
print(despues - antes)