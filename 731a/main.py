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

alpha = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))
a = I()
prev = "a"
# print(alpha)
ans = 0
for i in a:
    res = (alpha[i] - alpha[prev]) % 26
    if abs(res) > 13:
        res = abs(res - 26)
    ans += res
    # print(res)
    prev = i
print(ans)