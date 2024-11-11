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
    c = LII()
    prev = c[0]
    mn = float("inf")
    for i in c[1:]:
        tmp = i - prev
        if tmp < 0:
            print("0")
            break
        mn = min(tmp, mn)
        prev = i
    else:

        print(mn//2 + 1)