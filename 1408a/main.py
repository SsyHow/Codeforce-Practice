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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    b = II()
    L1 = LII()
    L2 = LII()
    L3 = LII()

    p = [L1[0]]

    for i in range(1, b-1):
        if L1[i] != p[i - 1]:
            p.append(L1[i])
            continue
        elif L2[i] != p[i - 1]:
            p.append(L2[i])
            continue

    if p[b-2] != L1[b-1] and p[0] != L1[b-1]:
        p.append(L1[b-1])
    elif p[b-2] != L2[b-1] and p[0] != L2[b-1]:
        p.append(L2[b-1])
    elif p[b - 2] != L3[b - 1] and p[0] != L3[b - 1]:
        p.append(L3[b - 1])
    print(*p)


