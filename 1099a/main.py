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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a, b = MII()
c, d = MII()
e, f = MII()

ans = a
for i in range(b, 0, -1):
    ans += i
    if i == d:
        ans -= c
    if i == f :
        ans -= e
    ans = max(ans, 0)
print(max(ans, 0 ))