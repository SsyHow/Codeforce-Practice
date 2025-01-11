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
    summ = 0
    for idx, i in enumerate(L):
        # print(idx, i, summ, idx , i - idx + summ, idx > i - idx + summ)
        if idx > i + summ:
            print("NO")
            break
        summ += i - idx
    else:
        print("YES")