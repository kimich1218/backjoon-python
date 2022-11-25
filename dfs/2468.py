import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

heights = [i for i in range(min(map(min, L)) - 1, max(map(max, L)))]

def dfs(x,y):

    visited[x][y] = True

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n and 0 <= ny < n):
            if visited[nx][ny] == False:
                dfs(nx,ny)

cnt = 0
max = 0

for height in heights:

    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if height >= L[i][j]:
                visited[i][j] = True

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfs(i,j)
                cnt += 1

    if max <= cnt:
        max = cnt
    
print(max)