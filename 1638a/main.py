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

    i = 0
    while i < b and i + 1 == L[i]:
        i += 1

    if i < b:
        l = i
        r = L.index(l+1) + 1
        # print(i, L[i])
        # print(r, L[r], L[:0], L[0:2][::-1])
        # print(L[:l])

        if len(L[:l]) > 0:
            print(*(L[:l]), end=' ')
        M = L[i:r][::-1]
        print(*(M), end=' ')
        print(*(L[r:]))
    else:
        print(*(range(1, b+1)), end = ' ')
        print()
