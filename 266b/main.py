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
c = I()
for i in range(b):
    if 'BG' not in c:
        break
    c = c.replace('BG', 'GB')
print(c)