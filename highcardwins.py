N = int(input())
bessie = []
elsie = []
flag = [False for i in range(2*N)]
for i in range(N):
  card = int(input())
  elsie.append(card)
  flag[card-1] = True
for i in range(2*N):
  if flag[i] == False:
    bessie.append(i+1)
bessie.sort(key = lambda x:-x)
elsie.sort(key = lambda x:-x)
count = 0
ans = 0
for i in range(N):
  if bessie[count]>elsie[i]:
    count += 1
    ans += 1
print(ans)
