import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline 

def dfs(v):

    visited[v] = 1

    for i in graph[v]:
        if(visited[i] != 1):
            dfs(i)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)