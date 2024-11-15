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
    mx = 9
    ans = ''
    b = II()
    while b > mx:
        ans = str(mx) + ans

        b -= mx
        mx -= 1
        # print(b)
    ans = str(b) + ans
    print(ans)