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

    prev = -1
    ans = ''
    for i in s:
        if i == '0':
            v = 1 if prev != 1 else 0
            ans += str(v)
            prev = v
        else:
            v = 1 if prev != 2 else 0
            ans += str(v)
            prev = v + 1
        # print(prev, ans)
    print(ans)