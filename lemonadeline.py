N = int(input())
cows = list(map(int,input().split()))
cows.sort(key = lambda x:-x)
# print(cows)
count = 0
if N == 0:
  print(0)
  exit()
for i in range(N):
  temp = cows[i]
  if temp >= i:
    count += 1
  else:
    print(count)
    exit()
print(count)
