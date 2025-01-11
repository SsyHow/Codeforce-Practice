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
    b= II()
    L = LII()
    for i in L:
        if i < 0:
            print("NO")
            break
    else:
        print("YES")
        print(101)
        print(*range(0, 101))
