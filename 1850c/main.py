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
    ans = ''
    for _ in range(8):
        b = I()

        for i in b:
            if 'a' <= i <= 'z':
                ans += i
    print(ans)