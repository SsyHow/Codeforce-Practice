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
    x, y, z = MII()
    if x == y == z:
        print("YES")
        continue
    print("YES" if x - y - z > 1 else "NO")