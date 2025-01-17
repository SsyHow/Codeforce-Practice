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
    b = II()
    L = LII()

    for i in range(b-1):
        x, y = sorted([L[i], L[i + 1]])
        if x * 2 > y:
            print("YES")
            break
    else:
        print("NO")