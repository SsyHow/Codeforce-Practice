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
    dic = Counter(L)

    for i in sorted(L):
        # dic[i] += 1

        if i != 0 and dic[i] > dic[i-1]:
            print("NO")
            break
    else:
        print("YES")
    # print(dic[99])

