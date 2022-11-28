import sys
sys.setrecursionlimit(10**9) 

r,c = map(int,sys.stdin.readline().split())

L = [list(map(str, sys.stdin.readline())) for _ in range(r)]
visited = set()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0

def dfs(x,y,cnt):

    global ans
    ans = max(ans, cnt)

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < r and 0 <= ny < c and not L[nx][ny] in visited):
            visited.add(L[nx][ny]) 
            dfs(nx,ny,cnt+1)
            visited.remove(L[nx][ny])

visited.add(L[0][0])
dfs(0,0,1)
print(ans)