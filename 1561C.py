for _ in range(int(input())):
  n = int(input())
  l, v, id = [], [], []
  for i in range(n):
    l.append(list(map(int, input().split()[1:])))
    cur, add = 0, 0
    for x in l[-1]:
      if cur <= x:
        add += x - cur + 1
        cur = x + 1
      cur += 1
    v.append(add)
    id.append(i)
  id.sort(key=lambda x: v[x])

  cur, add = 0, 0
  for i in id:
    for x in l[i]:
      if cur <= x:
        add += x - cur + 1
        cur = x + 1
      cur += 1
  
  print(add)
