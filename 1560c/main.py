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
    cor = int(b ** 0.5)
    if b == cor ** 2:
        print(cor, 1)
        continue
    elif b == cor ** 2 + 1:
        print(1, cor+1)
        continue

    mid = ((cor + 1) ** 2 - (cor ** 2 + 1)) // 2 + cor ** 2 + 1
    if b == mid:
        print(cor + 1, cor + 1)

    elif b < mid:
        print(b - (cor ** 2 + 1) + 1, cor + 1)
    else:
        # print((cor + 1) , (mid , b), "***")
        print(cor + 1, (cor + 1) - (b - mid))