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
if a & 1 == 0:
    if (a//2 - 1) & 1 == 0:
        print(a//2 - 2, a// 2 + 2)
    else:
        print(a//2 - 1, a// 2 + 1 )
else:
    print(a//2, a - a//2)