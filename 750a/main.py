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

a, b = MII()

n = 240

for i in range(a, -1, -1):
    if (i+1) * i // 2 * 5 <= n - b:
        print(i)
        break
else:
    print(0)
