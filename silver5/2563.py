N = int(input())
L = list()

for i in range(N):
    a,b = map(int, input().split())
    L.append((a,b))

square = 100 * N

for i in range(N):
    for k in range(i+1,N):

        length = abs(L[i][0] - L[k][0])
        width = abs(L[i][1] - L[k][1])

        if(0<= length <= 10 and 0 <= width <= 10):
            a = (10 - length) * (10 - width)
            square -= a

print(square)