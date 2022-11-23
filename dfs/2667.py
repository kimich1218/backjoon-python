n = int(input())
house = []

for _ in range(n):
    house.append(list(map(int, input())))

def dfs(x,y):

    if(x <= -1 or x >= n or y <= -1 or y >=n ):
        return False

    if house[x][y] == 1:
        global cntHouse
        cntHouse += 1

        house[x][y] = 0

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        
        return True

    return False

cnt = 0
cntList = []
cntHouse = 0

for x in range(n):
    for y in range(n):
        if(dfs(x,y) == True):
            cntList.append(cntHouse)
            cnt += 1
            cntHouse = 0

print(cnt)

cntList.sort()

for i in cntList:
    print(i)
