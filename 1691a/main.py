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
    odd = even = 0

    for i in MII():
        if i % 2== 0:
            even += 1
        else:
            odd += 1
    print(min(odd, even))