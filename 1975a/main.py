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
    M = sorted(L)
    for i in range(1, b):
        if L[i-1] > L[i]:
            k = L[i:] + L[:i]
            # print(k, M)
            if k == M:
                print("YES")
            else:
                print("NO")
            break
    else:
        print("YES")