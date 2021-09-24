dx,dy = dict(),dict()
for i in range(int(input())):
  x,y = map(int,input().split())
  if x in dx:
    dx[x].append(y)
  else:
    dx[x] = [y]
  if y in dy:
    dy[y].append(x)
  else:
    dy[y] = [x]
sx,sy = dict(),dict()
for i in dx:
  dx[i].sort()
  sx[i] = {}
  sx[i][dx[i][0]] = sum(dx[i])-dx[i][0]*len(dx[i])
  for j in range(1,len(dx[i])):
    sx[i][dx[i][j]] = sx[i][dx[i][j-1]]+(2*j-len(dx[i]))*(dx[i][j]-dx[i][j-1])
for i in dy:
  dy[i].sort()
  sy[i] = {}
  sy[i][dy[i][0]] = sum(dy[i])-dy[i][0]*len(dy[i])
  for j in range(1,len(dy[i])):
    sy[i][dy[i][j]] = sy[i][dy[i][j-1]]+(2*j-len(dy[i]))*(dy[i][j]-dy[i][j-1])
total = 0
for i in dx:
  for j in dx[i]:
    total += sx[i][j]*sy[j][i]
print(total%(10**9+7))
