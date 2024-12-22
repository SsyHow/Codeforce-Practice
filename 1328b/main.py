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
    n, k = MII()
    s = ['a' for _ in range(n)]

    for i in range(n-2, -1, -1):
        if k <= n - i - 1:
            s[i] = 'b'
            s[n-k] = 'b'
            print(''.join(s))
            break
        k -= n - i -1