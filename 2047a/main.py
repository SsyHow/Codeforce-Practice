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

a = II()
for _ in range(a):
    b = I()
    L = LII()
    k = 0
    s = 1
    ans = 0
    for i in L:
        k += i
        while k > s ** 2:
            s += 2
        if k == s ** 2:
            ans += 1
        # print(i, ans, k, s)
    print(ans)
