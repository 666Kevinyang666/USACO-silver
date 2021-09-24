import sys
sys.stdin = open("socdist.in")
sys.stdout = open("socdist.out",'w')
# n,k = map(int,input().split())
# pos = []
# for i in range(n):
#   num = int(input())
#   pos.append(num)
# pos.sort()

def check(x):
  count = 0
  temp = 0
  for i in range(n):
    if temp < pos[i]:
      temp = pos[i]+2*x
      count+=1
  if count<=k:
    return True
  return False

# low = 0
# high = pos[-1]
# while high-low>1:
#   mid = (high+low)//2
#   if check(mid):
#     high = mid
#   else:
#     low = mid
# print(high)

n,m = map(int,input().split())
coord = []
for i in range(m):
  a,b = map(int,input().split())
  coord.append([a,b])
coord.sort()
def check(x):
  count = 0
  temp = coord[0][0]
  for i in range(m):
    if temp < coord[i][0]:
      temp = coord[i][0]
    if temp<=coord[i][1]:
      count += (coord[i][1]-temp)//x+1
      temp += x*((coord[i][1]-temp)//x+1)
      if count>=n:
        return True
  return False
low,high = 0,coord[-1][1]
while high-low>1:
  mid = (high+low)//2
  if check(mid):
    low = mid
  else:
    high = mid
print(low)
