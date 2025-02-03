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
    b, c = MII()
    L = LII()

    ans = 0
    left = 0
    for i in L:
        ans += i // 2 * 2
        c -= i //2
        left += i & 1
    if left > c :
        ans += c * 2 - left
    else:
        ans += left
    print(ans)
