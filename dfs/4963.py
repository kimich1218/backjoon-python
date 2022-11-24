import sys
sys.setrecursionlimit(10000) 

def dfs(x,y):
    
    if(x <= -1 or x >= h or y <= -1 or y >= w):
        return False

    if g[x][y] == 1:

        g[x][y] = 0

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)

        return True

    return False


while(True):

    w, h = map(int, sys.stdin.readline().split())

    if(w == 0 and h == 0):
        break

    cnt = 0
    g = []

    for _ in range(h):
        a = list(map(int, sys.stdin.readline().split()))
        g.append(a)

    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                cnt += 1

    print(cnt)