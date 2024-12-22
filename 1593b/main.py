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
c = {'00', '50', '25', '75'}

def solve(b, i):
    pt = len(b) - 1

    ans = 0

    while pt >= 0 and b[pt] != i[1]:
        ans += 1
        pt -= 1

    if pt < 0: return float('inf')
    pt -= 1
    while pt >= 0 and b[pt] != i[0]:
        ans += 1
        pt -= 1

    return float('inf') if pt < 0 else ans


for _ in range(a):
    ans = float('inf')
    b = I()
    for i in c:
        ans = min(ans, solve(b, i))
    print(ans)