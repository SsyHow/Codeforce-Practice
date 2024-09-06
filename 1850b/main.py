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
    curr = -float('inf')
    for cnt in range(b):
        x, y = MII()
        if x <= 10:
            if curr < y:
                curidx = cnt
                curr = y
    print(curidx+1)