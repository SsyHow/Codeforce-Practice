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

for i in range(a):
    m = []
    # c = 0
    b = I()
    while len(m) < 8:
        b = I()
        m.append(list(b))
        # c += 1
    # for i in m:
    #     print(i)
    for x in range(1, 7):
        for y in range(1, 7):
            if m[x][y] == "#" and m[x - 1][y - 1] == "#" and m[x - 1][y + 1] == "#" and m[x + 1][y - 1] == "#" and \
                    m[x + 1][y + 1] == "#":
                print(x + 1, y + 1)



