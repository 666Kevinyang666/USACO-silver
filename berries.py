import sys
sys.stdin = open('berries.in','r')
sys.stdout = open('berries.out','w')
n, k = map(int, input().split())
fruits = list(map(int, input().split()))
ans = 0
for i in range(1,1001):
    a = 0  
    for j in range(n):
        a+=fruits[j]//i
    if a<k//2:
        break
    if a>=k:
        ans = max(ans,i*k//2)
        continue
    fruits.sort(reverse = True,key = lambda x:x%i)
    temp = (a-k//2)*i
    for j in range(k-a):
        if j>n-1:
            break
        temp+=fruits[j]%i
    ans = max(ans,temp)
print(ans)
