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
    L = LII()

    for i in range(1, b):
        if abs(L[i] - L[i-1]) != 5 and abs(L[i] - L[i-1]) != 7:
            print("NO")
            break
    else:
        print("YES")