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
    s = I()
    n = len(s)
    k = int(s, 2)
    c = s.find('0')

    if c != -1:
        c = n - c
        maxx, tmp = 0, 0
        for i in range(n-c):
            # print(s[i:i+c], int(s[i:i+c], 2), k, int(s[i:i+c]) ^k)
            if int(s[i:i+c], 2) ^ k > maxx:
                maxx, tmp = int(s[i:i+c], 2) ^ k, i
        print(1, n, tmp+1, tmp +c)
    else:
        print(1, n, n, n)