import sys
input=lambda:sys.stdin.readline()

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
    b = II()
    L = LII()
    # M = [0] * 26
    # ans = []
    #
    # for i in L:
    #     j = next(j for j in range(26) if M[j] == i)
    #     ans.append(chr(ord('a') + j))
    #     M[j] += 1
    #
    # print("".join(ans))
    d = {}
    r = ''

    for x in L:
        # print(d)
        c = d.get(x, 97)
        r += chr(c)
        d[x] = c + 1
    print(r)
