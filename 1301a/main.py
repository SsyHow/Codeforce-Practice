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
    x = I()
    y = I()
    z = I()
    n = len(x)
    for i in range(n):
        if z[i] != x[i] and z[i] != y[i]:
            print("NO")
            break
    else:
        print("YES")
