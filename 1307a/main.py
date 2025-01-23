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
    ans = L[0]
    for idx, i in enumerate(L[1:], start=1):
        if c < idx:
            break
        k = min(c // idx, i)
        # print("---", i, idx )
        # print(c,k, '****')
        ans += min(k, c)
        c -= k * idx

    print(ans)