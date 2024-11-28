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
    a, b, c = MII()
    newc = a + 2 * (b-a)
    newa = c - 2 * (c-b)
    newb = a + (c - a) // 2
    if newc >= c and newc %c == 0 and newc != 0:
        print("YES")


    elif newa >= a and newa % a == 0 and newa != 0:
        print("YES")

    elif newb>=b and (c-a) %2 == 0 and newb % b== 0 and newb != 0:
        print("YES")
    else:
        print("NO")