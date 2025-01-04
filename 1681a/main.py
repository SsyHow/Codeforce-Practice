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
    x = II()
    alice = LII()
    y = II()
    bob = LII()

    m, n = max(alice), max(bob)

    if m == n:
        print("Alice\nBob")

    elif m > n:
        print("Alice\nAlice")
    else:
        print("Bob\nBob")