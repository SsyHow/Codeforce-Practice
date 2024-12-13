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
    n = len(b)


    while n:
        start = chr(ord('a') + n - 1)


        if b[0] != start and b[-1] != start:
            break

        if b[0] == start:
            b = b[1:]
        elif b[-1] == start:
            b = b[:-1]

        n -= 1
    if b:
        print("NO")
    else:
        print("YES")
