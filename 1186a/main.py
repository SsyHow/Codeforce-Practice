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

a,b,c = MII()
if a <= b and a <= c:
    print("YES")
else:
    print("NO")