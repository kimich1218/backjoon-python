N = int(input())
L = []

for _ in range(N):
    a, b = map(int, input().split(" "))
    L.append((a, b))

for i in L:
    rank = 1
    for j in L:
        if(i[0] < j[0] and i[1] < j[1]):
            rank += 1
    print(rank)
