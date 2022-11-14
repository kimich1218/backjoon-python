T = int(input())
#0층 1호:1 2호:2 3호:3  4호:4
#1층 1호:1 2호:3 3호:6  4호:10
#2층 1호:1 2호:4 3호:10 4호:20
#3층 1호:1 2호:5 3호:15 4호:35

for _ in range(T):
    
    k = int(input())
    n = int(input())
    f = [i for i in range(1, n+1)] #0층 호수별 인원 수

    for _ in range(k):
        for i in range(n - 1):
            f[i+1] = f[i] + f[i + 1]
    print(f[n - 1])



