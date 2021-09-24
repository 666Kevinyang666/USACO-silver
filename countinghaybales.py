import sys
sys.stdin = open('haybales.in')
sys.stdout = open('haybales.out','w')
import heapq
N = int(input())
cows = []
for i in range(N):
  p,t = map(int,input().split())
  cows.append([i,p,t])
times = 0
max_times = 0
cows.sort(key=lambda x:x[1])
wait = []
i = 0
while i<N:
  if cows[i][1]>times and len(wait)>0:
    cow = heapq.heappop(wait)
    max_times = max(times-cow[1],max_times)
    times += cow[2]
  else:
    if times<cows[i][1]:
      times = cows[i][1]
    heapq.heappush(wait,cows[i])
    i+=1
print(max_times)
