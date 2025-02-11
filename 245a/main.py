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
s1 = s2 = 0
t1 = t2 = 0
for _ in range(a):
    t, x, y = MII()
    if t == 1:
        s1 += x
        t1 += 10
    else:
        s2 += x
        t2 += 10

print("LIVE" if s1 >= t1 // 2 else "DEAD")
print("LIVE" if s2 >= t2 // 2 else "DEAD")
