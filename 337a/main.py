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
L = LII()
L.sort()
mina = float('inf')
for i in range(b-a+1):
    mina = min((L[i+a-1] - L[i]) , mina)
print(mina)