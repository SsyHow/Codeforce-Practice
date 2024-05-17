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

for i in range(a):
    s = I()
    L = [s[i] for i in range(0, len(s), 2)]
    L.append(s[-1])

    print(''.join(L))