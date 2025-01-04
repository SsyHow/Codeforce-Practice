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


def find(L, le):
    ans = 0
    for i in range(1, le):
        ans += abs(L[i] - L[i-1])
    return ans
a = II()
for _ in range(a):
    b = II()
    L = LII()
    L.sort()
    L1 = L[:b]
    L2 = L[b:][::-1]
    ans = find(L1, b) + find(L2, b)
    vis = []

    for i in range(b):
        vis.append((L2[i], L1[i]))
    print(ans)
    for i in vis:
        print(*i)