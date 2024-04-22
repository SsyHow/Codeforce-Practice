import sys
def input():
    return sys.stdin.readline()

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
home = []
guest = []
for i in range(a):
    h, g = MII()
    home.append(h)
    guest.append(g)

ans = 0
for i in home:
    for j in guest:
        if i == j:
            ans += 1
print(ans)