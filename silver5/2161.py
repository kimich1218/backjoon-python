N = int(input())

a = [i for i in range(1, N + 1)]
b = [] # 버린 카드 담는 리스트
i = 0
while(i < N - 1):

    b.append(a[0])
    del a[0]

    a.append(a[0])
    del a[0]

    i += 1

c = b + a

for i in c:
    print(i, end=' ')