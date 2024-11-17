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
for  _ in range(a):
    c = "Yes" * 25
    b = I()
    if b in c:
        print("YES")
    else:
        print("NO")