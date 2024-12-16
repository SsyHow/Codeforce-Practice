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
    neg = 0
    num = {'+': 0, '-': 0, 0: 0}
    for i in range(len(L)):
        if L[i] > 0:
            num['+'] += 1

        elif L[i] < 0:
            num['-'] += 1
            if not neg:
                neg = i
        else:
            num[0] += 1

    if num[0] > 0 or num['-'] % 2 == 1:
        print(0)
    else:
        print(1)
        print(neg + 1, 0)

