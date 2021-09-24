N = int(input())
mon = []
for i in range(N):
  a,b = map(int,input().split())
  mon.append([a-b,a+b])
mon.sort(key = lambda x:(x[0],-x[1]))
maximum = mon[0]
res = 1
for i in range(N):
  if mon[i][1]>maximum[1]:
    res += 1
    maximum = mon[i]
print(res)
