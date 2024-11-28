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
ch = bi = ba = 0
L = LII()
for i in range(a):
    if i % 3 == 0:
        ch += L[i]
    elif i % 3 == 1:
        bi += L[i]
    else:
        ba += L[i]
# print(ch, bi, ba)
if ba == max(ch, bi, ba):
    print("back")
elif bi == max(ch, bi, ba):
    print("biceps")
else:
    print("chest")