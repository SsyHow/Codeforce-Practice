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
    L = LII()
    odd = []
    even = []

    for idx, i in enumerate(L):
        if i & 1 == 0:
            even.append(idx+1)
        elif i & 1 == 1:
            odd.append(idx+1)
        if len(odd) == 2:
            print(2)
            print(*odd)
            break
        if len(even) == 1:
            print(1)
            print(*even)
            break
    else:
        print(-1)

