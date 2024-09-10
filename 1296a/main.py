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
    b = II()
    L = LII()
    if len(L) % 2 == 1:
        for i in L:
            if i % 2 == 1:
                print("YES")
                break
        else:
            print("NO")
    else:
        one = False
        two = False
        for i in L:

            if i % 2== 1:
                one = True
            else:
                two = True
            if one and two:
                print("YES")
                break
        else:
            print("NO")