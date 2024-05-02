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
    n = II()
    a = []
    power = 1
    while n > 0:
        if n % 10 > 0:
            a.append(str((n%10) * power))
        n //= 10
        power *= 10
    print(len(a))
    print(' '.join(a))
