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

    if 3 ** (b-1) > 10 ** 9:
        print("NO")
    else:
        print("YES")
        print(*[3 ** i for i in range(b)])