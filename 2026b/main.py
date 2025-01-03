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
    ans = 0
    if b == 1:
        print(1)

    elif b & 1 == 0:
        for i in range(0, b, 2):
            ans = max(ans, L[i+1] - L[i])
        print(ans)
    else:
        k = []

        for i in range(b):
            tmp = 0
            M = L[:i] + L[i+1:]
            # print(M)
            for i in range(0, b-1, 2):
                tmp = max(tmp, M[i + 1] - M[i])
            k.append(tmp)
        # print(k)
        ans = min(k)

        print(ans)