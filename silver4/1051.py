N, M = map(int, input().split())

S = []
square = 1

for i in range(N):
    S.append(list(input()))

for i in range(N):
    for k in range(M):
        for length in range(1, min(N,M)):
            if(i+length < N and k + length < M):
                if(S[i][k] == S[i + length][k] == S[i][k + length] == S[i + length][k + length]):
                    area = (length + 1) ** 2 
                    if(area > square):
                        square = area

print(square)