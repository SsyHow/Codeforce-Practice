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
for _ in range(a):
    b = II()
    L = LII()

    i = b-1
    while i>=0 and L[i] == 1:
        i -= 1
    j = 0
    while j <= i and L[j] == 1:
        j += 1
    # print(i, j)
    print(i+1 - j+1 if i >= j else  0)
