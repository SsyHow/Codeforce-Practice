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

    s2 = (b + 2) // 3 + 1
    s1 = s2 - 1
    s3 = max(b - s2 - s1, 1)
    print(b- s2- s3,s2,s3)