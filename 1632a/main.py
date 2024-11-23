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
    b = II()
    c = I()
    if b == 1:
        print("YES")
    elif b == 2:
        print("YES") if c == '10' or c == '01' else print("NO")
    else:
        print("NO")
