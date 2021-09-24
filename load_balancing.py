import sys
sys.stdin = open('balancing.in')
sys.stdout = open('balancing.out','w')
n, b = map(int,input().split())
grid = [] 
for i in range(n):
  x, y = map(int,input().split())
  grid.append([x, y])
m = 1e9
for i in range(n):
  for j in range(n):
    q1,q2,q3,q4 = 0,0,0,0
    a,c = grid[i][0]-1,grid[j][1]-1
    for x,y in grid:
      if x>a and y>c:
        q1+=1
      if x>a and y<c:
        q2 += 1
      if x<a and y<c:
        q3 += 1
      if x<a and y>c:
        q4 += 1
    m = min(m,max(q1,q2,q3,q4))
print(m)
