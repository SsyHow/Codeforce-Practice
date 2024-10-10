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
    b,c = MII()
    ans = b*c // 2 if b*c % 2 == 0 else b*c // 2 + 1
    print(ans)