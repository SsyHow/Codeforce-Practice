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

n, m, a, b = MII()

print(min(n * a, (n+m-1)//m * b, (n - n // m * m) * a + n // m * b))