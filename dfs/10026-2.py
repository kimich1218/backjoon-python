import sys
sys.setrecursionlimit(10000) 

n = int(sys.stdin.readline())
L = [list(map(str, sys.stdin.readline())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    visited[x][y] = True

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n and 0 <= ny < n):

            if(not visited[nx][ny]):
                if L[x][y] == L[nx][ny]:
                    dfs(nx,ny)

cnt1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt1+=1

for i in range(n):
    for j in range(n):
        if(L[i][j] == 'R'):
            L[i][j] = 'G'

cnt2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt2+=1

print(cnt1, cnt2)