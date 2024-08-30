import sys

input = lambda: sys.stdin.readline()
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

from collections import defaultdict

a = II()
for _ in range(a):
    b = II()
    c = I().split()
    dic = defaultdict(int)
    for i in c:
        dic[i] += 1
        if dic[i] >= 3:
            print(i)
            # print(dic)
            break
    else:
        print(-1)