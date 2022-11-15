N = input()

T = [str(i) for i in range(10)]

numList = []

for i in range(10):
    cnt = 0
    for k in range(len(N)):
        if(T[i] == N[k]):
            cnt+=1
    numList.append(cnt)

t = int(numList[6]) + int(numList[9])

if(t % 2 == 1):
    t = t//2+1
else:
    t = t//2

del numList[6]
del numList[8]

numList.append(t)

print(max(numList))