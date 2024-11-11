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
for i in range(a):
    b = II()
    L = [0] * 26

    for i in I():
        L[ord(i) - ord("A")] += 1
    cnt = 0
    for idx, i in enumerate(L):
        if i > idx:
            cnt += 1
    # print(L)
    print(cnt)