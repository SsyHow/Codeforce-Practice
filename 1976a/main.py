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
    s = I()
    a = ''.join(sorted(s))
    print("YES") if s == a else print("NO")