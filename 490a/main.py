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
L = LII()

m = []
p = []
t = []
for idx, i in enumerate(L):
    if i == 1:
        m.append(idx)
    elif i == 2:
        p.append(idx)
    else:
        t.append(idx)

ans = list(zip(m, p, t))
print(len(ans))
for i in ans:
    x,y,z = i
    print(x+1, y+1, z+1)