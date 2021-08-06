N = int(input())
cows = []
graph = {}

for i in range(N):
  x,y,p = map(int,input().split())
  cows.append([x,y,p])
res = []
for i in range(N):
  graph[i] = []
  for j in range(N):
    count = 0
    d = ((cows[i][0]-cows[j][0])**2+(cows[i][1]-cows[j][1])**2)**0.5
    if d <= cows[i][2]:
      graph[i].append(j)
 
def dfs(x,graph):
  stack = []
  stack.append(x)
  seen = []
  seen.append(x)
  count = 0
  while stack:
    vertex = stack.pop()
    n = graph[vertex]
    for i in n:
      if i not in seen:
        stack.append(i)
        seen.append(i)
    count += 1
  return count

# dfs(0,graph)
temp = dfs(0,graph)
for a in range(N):
  if dfs(a,graph)>temp:
    temp = dfs(a,graph)
print(temp)
