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

n, m, a = MII()

l = n // a if n % a == 0 else n // a + 1
r = m // a if m % a == 0 else m // a + 1
print(l * r)