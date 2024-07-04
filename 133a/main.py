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

a = I()
if "H" in a or "Q" in a or "9" in a:
    print("YES")
else:
    print("NO")