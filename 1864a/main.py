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
    x, y, n = MII()
    yy = y
    L = [y]
    i = 1
    while n - 2:
        y -= i
        L.append(y)
        n -= 1
        i += 1
        # print(n)
        if n == 2:
            y -= i
            # print(y, x)
            if y < x:
                print(-1)
                break
            else:
                L.append(x)
    # print(L)
    else:
        print(*sorted(L))
