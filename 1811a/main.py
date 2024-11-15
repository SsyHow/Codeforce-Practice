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
    c = str(c)
    if  all([c <= i for i in s]):
        print(s + c)
    elif all([c > i for i in s]):
        print(c + s)
    else:
        for i in range(b):
            if s[i] < c:
                break
        # print(s[i], c)
        print(s[:i] + str(c) + s[i:])