for i in range(int(input())):
    n = int(input())
    out = 0
    d = {}
    mas = list(map(int, input().split()))
    m = sum(mas) / len(mas)
    for i in mas:
        if i not in d:
            d[i] = 0
        d[i] += 1
        if 2 * m - i in d:
            if 2 * m - i == i:
                out += d[i] - 1
            else:
                out += d[2 * m - i]
    print(out)
