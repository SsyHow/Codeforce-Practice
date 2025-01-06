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
    b = II()
    L1 = LII()
    L2 = LII()

    x, y = min(L1[-1], L2[-1]), max(L1[-1], L2[-1])

    for i in range(b):
        m, n = min(L1[i], L2[i]), max(L1[i], L2[i])
        if m <= x and n <= y:
            continue
        print("NO")
        break
    else:
        print("YES")


