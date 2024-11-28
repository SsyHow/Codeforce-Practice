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
    b = I()
    ones = b.count('1')
    zero = b.count('0')
    x = min(ones, zero)
    print("DA") if x % 2 else print("NET")