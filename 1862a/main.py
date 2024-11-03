def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

a = II()

for _ in range(a):
    n, m = MII()
    k = 0
    vika = 'vika'
    c = []
    for _ in range(n):
        c.append(list(I()))

    for i in range(m):
        if k >= 4:
            break
        for j in range(n):
            if c[j][i] == vika[k]:
                k += 1
                break
    print("YES") if k == 4 else print("NO")