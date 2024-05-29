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

for i in range(a):
    ans = 0
    b = I()
    c = "codeforces"

    for j in range(10):
        if b[j] != c[j]:
            ans += 1
    print(ans)