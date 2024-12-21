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
    ans = sorted(set(L))
    # print(ans)
    for i in set(L):
        tmp = [i] * (L.count(i) - 1)
        # print(tmp)
        for j in tmp:
            ans.append(j)
    print(*ans, sep=' ')

