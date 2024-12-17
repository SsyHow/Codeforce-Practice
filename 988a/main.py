
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
ans = []
vis = set()

for idx, x in enumerate(L):
    if x not in vis:
        vis.add(x)
        ans.append(idx + 1)
    if len(ans) == b:
        print("YES")
        print(*ans, sep = ' ')
        break
else:
    print("NO")