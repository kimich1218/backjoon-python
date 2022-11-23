computerNumber = int(input())
computerConnectionNumber = int(input())

computerGraph = [[] for _ in range(computerNumber + 1)]
visited = [0] * (computerNumber + 1)

for _ in range(computerConnectionNumber):
    a, b = map(int, input().split())
    computerGraph[a]+=[b]
    computerGraph[b]+=[a]

print(computerGraph)

def dfs(v):
    visited[v] = 1
    print(v,end='')
    for i in range(1,computerNumber + 1):
        if i in computerGraph[v]:
            if not visited[i]:
                dfs(i)

dfs(1)


