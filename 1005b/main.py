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

s = I()
j = I()

n = len(s)
m = len(j)

c = min(n, m)
i = -1
while i >= -c:
    if s[i] != j[i]:
        break
    i -= 1

print(n+i+m+i + 2)
