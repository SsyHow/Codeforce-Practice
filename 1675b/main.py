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
    for i in range(b-2, -1, -1):
        while L[i] >= L[i+1] and L[i] > 0:
            L[i] //= 2
            ans += 1

        if L[i] == L[i+1]:
            print(-1)
            break
    else:
        print(ans)