N,M = map(int,input().split())
adjList = dict()
#build adjacency list
for i in range(M):
    u,v = map(int,input().split())
    if u not in adjList:
        adjList[u]=[]
    if v not in adjList:
        adjList[v]=[]
    adjList[u].append(v)
    adjList[v].append(u)

def dfs(v,visited):
    visited[v]=True
    for i in adjList[v]:
        if not visited[i]:
            dfs(i,visited)

nodes = [i for i in range(1,1+N)]#剩余的节点
# print(nodes)

result = []
for i in range(N):
    v = int(input())

    visited = [False for i in range(N+1)]

    dfs(v,visited)

    #检查是否联通
    flag =True
    for i in nodes:
        if not visited[i]:
            flag = False
    result.append("YES" if flag else "NO")
    for i in adjList[v]:
        adjList[i].remove(v)
    del adjList[v]
    nodes.remove(v)
for i in result:
    print(i)
