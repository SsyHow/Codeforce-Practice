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
    M = [L[i] - L[i-1] for i in range(1, b)]
    # print(M)
    for i, x in enumerate(M):
        if x < 0 and i & (i + 1) != 0:
            print("NO")
            break
    else:
        print("YES")