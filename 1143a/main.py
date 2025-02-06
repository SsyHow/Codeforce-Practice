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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
L = LII()
ones = L.count(1)
zero = L.count(0)
l = r = 0

for idx, i in enumerate(L):
    if i == 0:
        l += 1
        if l == zero:
            print(idx+1)
            break
    else:
        r += 1
        if r == ones:
            print(idx+1)
            break