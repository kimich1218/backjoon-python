N = int(input())
numCount = 0

for i in range(1,N+1):
    numCount += len(str(i))
print(numCount)
