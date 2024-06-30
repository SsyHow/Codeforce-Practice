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

if a % 2 == 0:
    print(a //2)
    print(' '.join(['2'] * (a//2)))
else:
    print((a-3)//2 + 1)
    L = ['2'] * ((a-3) // 2)
    L.append('3')
    print(' '.join(L))