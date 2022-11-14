n , m = map(int, input().split())
a = [i for i in range(2,n+1)]
# a = [2,3,4,5,6,7]
cnt = 0
print(a)
while(len(a) != 0):

    f = a[0]

    b = a

    for i in range(len(a)):
        if(b[i] % f == 0):
            cnt+=1
            if(cnt == m):
                print(a[i])
                break
            a[i] = 0

    for i in a:
        if i == 0:
            a.remove(0)