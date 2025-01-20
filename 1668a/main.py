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
    b, c = MII()

    if b < c:
        b, c = c, b
    if c == 1 and b > 2:
        print(-1)

        continue

    if c == b:
        print((b-1)*2)

        continue

    print((c - 1) * 2 + 1 + ((b - c - 1)//2) * 4 + (b - c - 1)%2 * 3)

