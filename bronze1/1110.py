a = int(input())
cnt = a

#append

for _ in range(a):
    w = input()
    
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            pass
        else:
            if w[i] in w[i+1:]:
                cnt -= 1
                continue

print(cnt)
