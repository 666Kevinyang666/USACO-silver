n,g = map(int,input().split())
cows = []
for i in range(n):
  a,b,c = map(int,input().split())
  cows.append((a,b,c))
cows.sort()
cow_milk = {0:0}
total = 0
for i in cows:
  temp = max(cow_milk.values())
  num = list(cow_milk.values()).count(temp)
  old_change = list(cow_milk.keys())[list(cow_milk.values()).index(temp)]
  if i[1] in cow_milk:
    cow_milk[i[1]]+=i[2]
  else:
    cow_milk[i[1]]=i[2]
  # print(cow_milk)
  maxs = max(cow_milk.values())
  count = list(cow_milk.values()).count(maxs)
  # for x,y in enumerate()
  change = list(cow_milk.keys())[list(cow_milk.values()).index(maxs)]
  if (maxs!=temp and old_change!=change) or (maxs == temp and num!=count):
    total += 1
print(total)
