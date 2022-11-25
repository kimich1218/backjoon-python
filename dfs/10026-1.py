import sys
sys.setrecursionlimit(10000) 

n = int(sys.stdin.readline())
L = [list(map(str, sys.stdin.readline())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x,y):

    if(x <= -1 or x >= n or y <= -1 or y >= n):
        return False

    if(not visited[x][y]):

        visited[x][y] = True

        if x-1 >= 0:
            if(L[x][y] == L[x-1][y]):
                dfs(x-1,y)
        if y-1 >= 0:  
            if(L[x][y] == L[x][y-1]):  
                dfs(x,y-1)
        if x+1 < n:
            if(L[x][y] == L[x+1][y]):
                dfs(x+1,y)
        if y+1 < n:
            if(L[x][y] == L[x][y+1]):
                dfs(x,y+1)


cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(n):
    for j in range(n):

        if(not visited[i][j]):

            if L[i][j] == 'R':
                dfs(i,j)
                cnt1 += 1

            if L[i][j] == 'G':
                dfs(i,j)
                cnt2 += 1

            if L[i][j] == 'B':
                dfs(i,j)
                cnt3 += 1

print(cnt1+cnt2+cnt3, end=' ')

for i in range(n):
    for j in range(n):
        if(L[i][j] == 'R'):
            L[i][j] = 'G'

cnt1 = 0
cnt2 = 0
cnt3 = 0

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):

        if(not visited[i][j]):

            if L[i][j] == 'R':
                dfs(i,j)
                cnt1 += 1

            if L[i][j] == 'G':
                dfs(i,j)
                cnt2 += 1

            if L[i][j] == 'B':
                dfs(i,j)
                cnt3 += 1

print(cnt1+cnt2+cnt3)