
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
    n, m, rb, cb, rd, cd = MII()
    if rb == rd or cb == cd:
        print(0)
        continue
    c = rd - rb if rb < rd else n*2 - rb - rd
    d = cd - cb if cb < cd else m*2 - cd - cb
    print(min(c, d))