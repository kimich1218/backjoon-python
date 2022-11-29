import sys
sys.setrecursionlimit(10000000)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for _ in range(n - 1):

    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):

    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2, n + 1):
    print(visited[i])