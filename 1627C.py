t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] * (n+1)
    e = [[] for _ in range(n+1)]
    for i in range(n-1):
        u, v = map(int, input().split())
        a[u] += 1
        a[v] += 1
        e[u].append((v, i))
        e[v].append((u, i))
    if any(i > 2 for i in a):
        print(-1)
        continue
    ans = [0] * (n-1)
    cur = a.index(1)
    last = -1
    for i in range(n-1):
        for v, j in e[cur]:
            if v != last:
                ans[j] = [3, 2][i&1]
                last, cur = cur, v
                break
    print(*ans)
