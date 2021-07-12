import sys
sys.setrecursionlimit(10000+13)
w,l = map(int,input().split())
matrix = []
total = 0
final = [[0 for i in range(l)]for i in range(w)]
for i in range(w):
  line = input()
  matrix.append(line)
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
def dfs(x,y):
  final[x][y] = 1
  for i in range(8):  
    tx = dx[i]+x
    ty = dy[i]+y
    if tx >= w or ty >= l:
      continue
    if tx<0 or ty<0:
      continue
    if matrix[tx][ty] == '.' or final[tx][ty] == 1:
      continue
    dfs(tx,ty)
res = 0
for i in range(w):
  for j in range(l):
    if matrix[i][j] == 'W' and final[i][j] == 0:
      dfs(i,j)
      res+=1
print(res)
