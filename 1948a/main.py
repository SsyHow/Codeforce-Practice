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
    if b % 2 == 0:
        c = "AABB" * 50
        print("YES")
        print(c[:b])
    else:
        print("NO")