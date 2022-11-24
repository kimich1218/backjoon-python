import sys 
sys.setrecursionlimit(10000) 


def bfs(x, y):

    if(x <= -1 or x >= n or y <= -1 or y >= m):

        return False

    if L[x][y] == 1:
        L[x][y] = 0

        bfs(x-1,y)
        bfs(x,y-1)
        bfs(x+1,y)
        bfs(x,y+1)

        return True

    return False

t = int(input())
cnt = 0

for _ in range(t):

    cnt = 0

    m, n, k = map(int, input().split())

    L = [[0] *  m  for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        L[b][a] = 1

    for i in range(n):
        for j in range(m):
            if bfs(i,j) == True:
                cnt += 1
    print(cnt)

