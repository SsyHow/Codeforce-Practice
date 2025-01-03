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

def check(M):
    return M[2] - M[0]

a = II()
for _ in range(a):
    b = II()
    L = LII()
    L.sort()
    ans = float('inf')
    for i in range(b-2):
        ans = min(ans, check(L[i:i+3]))
        # print(L[i:i+3], ans, check(L[i:i+3]))
    print(ans)