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
    c = I()
    ans = 0
    x = 0
    dic = {0:1}
    for i in c:
        x += int(i) - 1
        ans += dic.get(x, 0)
        dic[x] = dic.get(x, 0) + 1
    print(ans)