
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
    x,y,z = MII()
    b = x + z//2 + 1 if z%2 != 0 else x + z//2
    c = y + z//2

    if b > c:
        print("First")
    else:
        print("Second")