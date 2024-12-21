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
    if b == 1 or c == 1:
        print("YES")
    else:
        print("YES") if b== 2 and c == 2 else print("NO")