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
s1 = I()
s2 = I()
cnt = 0
for i in range(a):
    a, b = int(min(s1[i], s2[i])), int(max(s1[i], s2[i]))
    cnt += min(b-a, a+10 - b)
print(cnt)