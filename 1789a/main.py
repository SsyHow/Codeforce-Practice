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

from math import gcd
a = II()
for _ in range(a):
    b = II()
    L = LII()
    # vis = float('inf')
    flag = False
    for i in range(b):
        for j in range(i+1, b):

            if gcd(L[i], L[j]) <= 2:
                # print(L[i] , L[j], gcd(L[i] < L[j]) , b, gcd(L[i] < L[j]) < b)
                print("YES")
                flag = True
                break
        if flag:
            break
    else:
        print("NO")


