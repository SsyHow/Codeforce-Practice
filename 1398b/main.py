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
    s = sorted(I().split('0'), key=lambda x: -len(x))

    ans = 0
    # print(s)
    for i in range(len(s)):
        if i % 2== 0:
            ans += len(s[i])

    print(ans)





