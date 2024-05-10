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
mia = 0
chi = 0
for i in range(a):
    b, c = MII()
    if b > c:
        mia += 1
    elif c > b:
        chi += 1
if mia == chi:
    print("Friendship is magic!^^")
elif mia > chi:
    print("Mishka")
else:
    print("Chris")