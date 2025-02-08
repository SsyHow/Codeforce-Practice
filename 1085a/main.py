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

s = I()

n = len(s)
L = []

if n & 1 == 0:
    l, r = n // 2 - 1, n // 2
    while l >= 0:
        L.append(s[l])
        L.append(s[r])
        l -= 1
        r += 1
else:
    L.append(s[n//2])
    l, r = n // 2 - 1, n // 2 + 1
    while l >= 0 :
        L.append(s[r])

        L.append(s[l])
        l -= 1
        r += 1
print(''.join(L))


