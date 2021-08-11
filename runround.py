M = int(input())
def runaround(num):
    num = list(map(int,str(num)))
    if len(set(num))!=len(num):
        return False
    count,index = 0,0
    seen = [False]*len(num)
    while count<len(num):
        index = (index+num[index])%len(num)
        if seen[index]:
            break
        else:
            seen[index] = True
            count+=1
    return count==len(num) and index == 0
Flag = False
while not Flag:
    M += 1
    Flag = runaround(M)
print(M)
