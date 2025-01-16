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
b = II()
L = []
for _ in range(a):
    L.append(II())
L.sort(reverse=True)
ans = i = 0
while ans < b:
    ans += L[i]
    i += 1
print(i)

