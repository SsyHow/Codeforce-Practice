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
    bb = II()
    s = I()
    t = I()

    r = b = 0

    for i in range(bb):
        # print(s[i] > t[i], s[i] , t[i])
        if s[i] > t[i]:
            r += 1
        elif s[i] < t[i]:
            b += 1

    if r == b:
        print("EQUAL")
    elif r > b:
        print("RED")
    else:
        print("BLUE")