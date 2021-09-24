import sys
sys.stdin = open('herding.in')
sys.stdout = open('herding.out','w')
N = int(input())
cows = []
for i in range(N):
  cows.append(int(input()))
cows.sort()
if cows[-1]-cows[0] == N-1:
  print(0)
  print(0)
  exit()
def pre(lst):
  num_list = [0]
  for i in lst:
    num_list.append(num_list[-1]+i)
  return num_list
nums = [0 for i in range(N)]
for i in range(N):
  j=i
  while cows[j]<=cows[i]+N-1:
    j+= 1
    nums[i]+= 1
    if cows[j-1] == cows[-1]:
      break
def max_times(lst):
  count = max(lst[-2]-lst[0],lst[-1]-lst[1])
  return count-N+2
if cows[-2]-cows[0] == N-2 and cows[-1]-cows[-2]>2:
  print(2)
  print(max_times(cows))
  exit()
if cows[-1]-cows[1] == N-2 and cows[1]-cows[0]>2:
  print(2)
  print(max_times(cows))
  exit()

print(N-max(nums))
print(max_times(cows))
