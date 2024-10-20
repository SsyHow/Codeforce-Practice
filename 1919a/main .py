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
for _ in range(II()):
    a, b = MII()
    if (a + b) % 2 == 0:
        print("Bob")
    else:
        print("Alice")