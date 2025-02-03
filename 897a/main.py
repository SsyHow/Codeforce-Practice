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

a, b = MII()
s = I()
s = list(s)
for _ in range(b):
    l, r, c1, c2 = LI()
    l = int(l)
    r = int(r)
    for i in range(l-1, r):
        if s[i] == c1:
            s[i] = c2
print(''.join(s))