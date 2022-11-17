N = int(input())

paper = [[0]*100 for i in range(100)]

for _ in range(N):
    x, y= map(int,input().split())
    for i in range(x,x+10):
        for k in range(y,y+10):
            paper[i][k] = 1

area = 0

for paper_num in paper:
    area += paper_num.count(1)

print(area)
