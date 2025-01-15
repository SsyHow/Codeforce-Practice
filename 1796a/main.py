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

a = 1000
L = []
for i in range(a):
    if i % 3 == 0:
        L.append('F')
    if i % 5 == 0:
        L.append('B')
k = ''.join(L)
a = II()
for _ in range(a):
    b = II()
    s = I()
    print("YES" if s in k else "NO")