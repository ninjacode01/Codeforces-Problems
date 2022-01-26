for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans= 0
    for i in range(n-(2*k),n-k):
        ans += a[i]//a[i+k]
    for j in range(0,n-(2*k)):
        ans+= (a[j])
    print(ans)
