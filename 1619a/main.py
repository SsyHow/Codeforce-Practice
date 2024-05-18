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
for i in range(a):
    b = I()
    length = len(b)
    if b[:length//2] == b[length//2:]:
        print("YES")
    else:
        print("NO")