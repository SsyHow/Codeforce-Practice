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

t = II()
ans = 0
for _ in range(t):
    a, b, x, y = MII()
    ans = 0
    if x > 0:
        ans = max(ans, (x) * b)
    if x < a- 1:
        ans = max(ans, (a - x - 1) * b)
    if y > 0:
        ans = max(ans, (y) * a)
    if y < b - 1:
        ans = max(ans, (b - y - 1) * a)
    print(ans)

