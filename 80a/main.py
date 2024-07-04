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

L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

n, m = MII()
try:

    n = L.index(n)
    m = L.index(m)
    if n == m - 1:
        print("YES")
    else:
        print("NO")
except:
    print("NO")
