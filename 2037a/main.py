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
for _ in range(a):
    b = II()
    L = LII()
    dic = {}
    ans = 0
    for i in range(b):
        # print(i, L, b)
        if L[i] not in dic:
            dic[L[i]] = 1

        elif dic[L[i]] == 0:
            dic[L[i]] += 1
        else:
            dic[L[i]] -= 1
            ans += 1
    print(ans)
