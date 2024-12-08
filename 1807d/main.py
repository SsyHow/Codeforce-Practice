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
    tmp = 0
    prefix = []
    for i in L:
        tmp += i
        prefix.append(tmp)

    for _ in range(c):
        x, y, k = MII()
        x -= 1
        y -= 1
        # print((prefix[y] - prefix[x]) % 2 , (k * (y-x+1)) % 2)
        # print(prefix[y],  prefix[x])

        c =(prefix[y] - prefix[x-1]) % 2 if x >= 1 else prefix[y] % 2
        if c == (k * (y-x+1)) % 2:
            print("YES") if prefix[-1] % 2 == 1 else print("NO")
        else:
            print("YES") if prefix[-1] % 2 == 0 else print("NO")
