import sys
sys.stdin = open('citystate.in','r')
sys.stdout = open('citystate.out','w')
N = int(input())
cities = dict()
res = 0
for i in range(N):
  city,code = input().split()
  if city[:2]!= code:
    key = city[:2] + code
    if key not in cities:
      cities[key] = 0
    cities[key] += 1
for key in cities:
  if key[2:] + key[:2] in cities:
    res += cities[key]*cities[key[2:]+key[:2]]
print(res//2)
