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
    b, c = MII()
    s = I()
    t = I()
    s += t[::-1]
    print("YNEOS"[s.count('BB') + s.count('RR') + s.count('RRR') + s.count("BBB") > 1::2])