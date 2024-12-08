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

n = II()
for _ in range(n):
    k = II()
    a = I()
    b = I()
    c = I()
    for i in range(k):
        if c[i] != a[i] and c[i] != b[i]:
            print("YES")
            break
    else:
        print("NO")