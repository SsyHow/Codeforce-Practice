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

a  = II()
for _ in range(a):
    s = I()
    L = sorted(s)
    idx = 0
    for i in range(1, len(L)):

        if ord(L[i]) - ord(L[idx]) != 1:
            print("NO")
            break
        idx = i
    else:
        print("YES")