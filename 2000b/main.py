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
    l = r = L[0]
    for i in L[1:]:
        if i == l-1:
            l -= 1

        elif i == r + 1:
            r += 1
        else:
            print("NO")
            break
    else:
        print("YES")