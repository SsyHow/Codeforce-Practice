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
from collections import Counter
a = II()
for _ in range(a):
    b = II()
    L = LII()

    fre = [0] * (b + 1)
    for i in L:

        fre[i] += 1
    tmp = b -2
    # print(fre)
    for idx, i in enumerate(fre):
        if i == 0:
            continue
        if idx == tmp/idx and fre[idx] > 1:
            print(idx, idx)
            break
        elif idx != tmp/idx and tmp%idx == 0 and fre[tmp//idx] >= 1:
            # print(idx)
            print(idx, tmp//idx)
            break
