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
    x, y, m, n = MII()
    s = ''
    for i in range(1, 13):
        if i == x or i == y:
            s += 'a'
        elif i == m or i == n:
            s += 'b'

    if s == 'abab' or s == 'baba':
        print("YES")
    else:
        print("NO")


