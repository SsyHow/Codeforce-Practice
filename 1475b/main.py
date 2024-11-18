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
    c = b // 2020

    if c == 0:
        print("NO")
    elif c*2020 <= b <= c*2021:
        print("YES")
    else:
        print("NO")
