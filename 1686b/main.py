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
    c = LII()

    i = 0
    ans = 0
    while i < b-1:
        if c[i] > c[i+1]:
            ans += 1
            i += 1
        i += 1
    print(ans)