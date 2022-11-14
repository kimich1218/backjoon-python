a,b,c = 0,0,0

time = int(input())

if(time%10 == 0):
    if(time // 300 != 0):
        a = time // 300
        time = time % 300
        
        if(time // 60 != 0):
            b = time // 60
            time = time % 60
            c = time //10 
        else:
            c = time // 10
    else:
        if(time // 60 != 0):
            b = time // 60
            time = time % 60
            c = time // 10
        else:
            time = time // 10
            c = time
    print(a, b, c)
    
else:
    print(-1)