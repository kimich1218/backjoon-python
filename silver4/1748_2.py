N = int(input())

M = len(str(N)) - 1

count = 0

9
90
900

for i in range(M):
    count += 9 * (10 ** i) * (i + 1)

h = (N - (10 ** M - 1)) * (M+1)
print(count + h)