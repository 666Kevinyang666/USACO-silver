import heapq
C,N=map(int,input().split())
chickent=[]
for i in range(C):
    chickent.append(int(input()))
chickent.sort()
cowt=[]
for i in range(N):
    a,b=list(map(int,input().split()))
    cowt.append([b,a])
cowt.sort(key=lambda x:x[1])

pairs=0
cow_index=0
heap=[]

for i in range(C):
    #到的比鸡早的牛
    while cow_index<N and chickent[i]>=cowt[cow_index][1]:
        heapq.heappush(heap,cowt[cow_index])
        cow_index+=1
    #在鸡到之前走了的牛从heap删掉
    while heap and chickent[i]>heap[0][0]:
        heapq.heappop(heap)
            
    if heap:
        heapq.heappop(heap)
        pairs+=1

print(pairs)
