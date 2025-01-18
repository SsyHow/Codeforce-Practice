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
    L = LII()
    ans = []
    for i in range(c):
        tmp = [(x >> (c-1-i)) & 1 for x in L]
        ans.append('1') if tmp.count(1) > tmp.count(0) else ans.append('0')
    # print(ans)
    print(int(''.join(ans),2))
