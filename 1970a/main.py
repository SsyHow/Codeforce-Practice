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

a = I()

L = []
cnt = 0
for i in a:
    L.append(cnt)
    if i == '(':
        cnt += 1
    else:
        cnt -= 1

z = zip(a, range(1, len(a)+1), L)


z = sorted(z, key=lambda x: (x[2], -x[1]))
c = ''.join([i[0] for i in z])
print(c)