def my_factorial(n):
    m = 1
    for i in range(1, n+1):
        m = m * i
    return m

n, k = map(int,input().split())

print(my_factorial(n)//my_factorial(k)//my_factorial(n-k))