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
for i in range(a):
    b = I()
    if len(set(b)) > 1:
        print("YES")
        print(b[1:] + b[0])
    else:
        print("NO")