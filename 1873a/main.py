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


dic = {'abc', 'acb', 'bac', 'cba'}

a = II()
for i in range(a):
    b = I()
    if b in dic:
        print("YES")
    else:
        print("NO")