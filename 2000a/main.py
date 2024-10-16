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

for _ in range(II()):
    b = II()
    if 102 <= b <=109 or 1010<= b <= 1099:
        print("YES")
    else:
        print("NO")
