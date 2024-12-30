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
    b, c = MII()
    L = LII()
    M = ['B' for _ in range(c)]

    for i in L:
        i -= 1
        mm = min(i, c - i - 1)
        nn = max(i, c - i - 1)
        if M[mm] =='B':
            M[mm] = 'A'
        elif M[nn] =='B':
            M[nn] = 'A'
    print("".join(M))