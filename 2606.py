computerNumber = int(input())
computerConnectionNumber = int(input())

computerGraph = [[0] * (computerNumber + 1) for _ in range(computerNumber + 1)]
visited = [0] * ( computerNumber + 1)

for _ in range(computerConnectionNumber):
    a, b = map(int, input().split())
    computerGraph[a][b] = computerGraph[b][a] = 1

print(computerGraph)

computerCount = 0

def dfs(v):
    global computerCount
    visited[v] = 1
    for i in range(1,computerNumber + 1):
        if visited[i] == 0 and computerGraph[v][i] == 1:
            dfs(i)
            computerCount += 1


dfs(1)

print(computerCount)

