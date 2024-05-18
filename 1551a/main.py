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
    num = II()
    two = num // 3
    one = num - two * 2
    if one - two >= 2:
        one, two = one - 2, two + 1
    print(one, two)