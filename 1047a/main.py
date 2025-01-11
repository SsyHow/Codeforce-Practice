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

print(f"1 1 {a-2}" if (a-2) % 3 else f"1 2 {a-3}")