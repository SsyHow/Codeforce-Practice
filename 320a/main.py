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
while a > 0:
    if (a - 144) % 1000 == 0:
        a = (a - 144) // 1000
    elif (a - 14) % 100 == 0:
        a = (a - 14) // 100
    elif (a - 1) % 10 == 0:
        a = (a - 1) // 10
    else:
        break
print("YES") if a == 0 else print("NO")