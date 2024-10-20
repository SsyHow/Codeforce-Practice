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
    top, sec = sorted(L[:2], reverse=True)
    for i in L[2:]:
        # print(top, sec)
        if i >= top:
            sec = top
            top = i
        elif i > sec:
            sec = i
    # print(top, sec)
    for i in L:
        if i < top:
            print(i - top, end=' ')
        else:
            print(top - sec, end=' ')
    print()