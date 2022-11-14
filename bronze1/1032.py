a = int(input())
firstWord = list(input())
firstWorldLen = len(firstWord)

for i in range(a-1):
    otherWord = list(input())
    for j in range(firstWorldLen):
        if(firstWord[j] != otherWord[j]):
            firstWord[j] = '?'

print(''.join(firstWord))
