switchNumbers = int(input())
switchList = list(map(int, input().split()))
studentNumbers = int(input())


for _ in range(studentNumbers):
    
    a, b = map(int, input().split())

    #남자
    if(a == 1): 
        for k in range(switchNumbers):
            if (k + 1) % b == 0:

                if switchList[k] == 0:
                    switchList[k] = 1
                
                else:
                    switchList[k] = 0
    # 여자    
    if(a == 2):

        if switchList[b-1] == 0:
            switchList[b-1] = 1
        else:
            switchList[b-1] = 0
        
        for i in range(1, switchNumbers // 2):
            

            if((b-1) - i >= 0 and (b-1) + i <switchNumbers):
                

                if switchList[(b-1) - i] == switchList[(b-1) + i]:

                    if switchList[(b-1) -i] == 0:
                        switchList[(b-1)-i] = 1
                        switchList[(b-1) + i] = 1
                    else:
                        switchList[(b-1)-i] = 0
                        switchList[(b-1) + i] = 0
                else:
                    break
            else:
                break


for i in range(switchNumbers):
    print(switchList[i], end = " ")
    if (i+1) % 20 == 0:
        print()

