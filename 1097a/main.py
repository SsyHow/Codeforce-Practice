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
L = LI()
for i in L:
    if i[0] == a[0]:
        print("YES")
        break
    elif i[1] == a[1]:
        print("YES")
        break
else:
    print("NO")