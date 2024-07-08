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
    ans = 0
    lim = II()
    dic = 1
    while dic <= lim:
        # print(dic)
        for j in range(1, 10):
            # print(j , x, a)
            if j * dic > lim:
                break
            ans += 1
        dic += 10 ** len(str(dic))

    print(ans)