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

def check(s):
    s = str(s)
    return len(s) == len(set(s))

a, b = MII()
for i in range(a, b+1):
    if check(i):
        print(i)
        break
else:
    print(-1)