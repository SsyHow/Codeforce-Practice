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

n, d = MII()
tmp = ans = 0
for i in range(d):
    s = I()
    # print([int(i) for i in list(s)])
    if sum([int(i) for i in list(s)]) == n:
        ans = max(ans, tmp)
        tmp = 0
    else:
        tmp += 1
ans = max(ans, tmp)
print(ans)