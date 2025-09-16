def fibonacci(n, i, j, k):
    if n == 0:
        return k
    
    k = i + j
    i = j
    j = k
    n -= 1
    #print(k, n)
    return fibonacci(n, i, j, k)

i = 0
j = 1
k = 0

n = int(input()) - 2

print(fibonacci(n, i, j, k))