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
    n = II()
    arr = [int(i) for i in I()]

    ans, c, f = True, 0, False

    for i in range(n//2):
        if arr[i] != arr[n-i-1]:
            c += 1
            if f:
                ans = False
        elif c > 0:
            f = True
    print("YES") if ans else print("NO")