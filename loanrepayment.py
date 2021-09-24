import sys
sys.stdin = open('loan.in')
sys.stdout = open('loan.out','w')
n,k,m = map(int,input().split())
def check(x):
  global m
  g = 0
  d = k
  while d>0:
    y = (n-g)//x
    if y<=m:
      g+=d*m
      return g>=n
    same = (n-g-x*y)//y
    if same+1<d:
      d -= same+1
      g+=(same+1)*y
    else:
      g+=y*d
      break
    if g>=n:
      return True
  return False
# print(check(2))
low,high = 0,n
while high-low>1:
  mid = (high+low)//2
  if check(mid):
    low = mid
  else:
    high = mid
print(low)
n,k = map(int,input().split())
num = []
for i in range(n):
  a = int(input())
  num.append(a)
num.sort()
if sum(num)<k:
  print(0)
  exit()
def check(x):
  count = 0
  for i in range(n):
    count+=num[i]//x
  if count>=k:
    return True
  return False
low = 1
high = sum(num)
while high-low>1:
  mid = (low+high)//2
  if check(mid):
    low = mid
  else:
    high = mid
print(low)
