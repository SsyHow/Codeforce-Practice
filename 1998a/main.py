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
    x, y, n = MII()
    ans = [[x, y]] if n & 1 == 1 else []

    for i in range(1, n // 2+1):
        ans.append([x - i, y - i])
        ans.append([x + i, y + i])
    # print(ans, "********")
    for i in ans:
        print(*i, sep = ' ')