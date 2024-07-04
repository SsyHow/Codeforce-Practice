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
L = LII()
L.sort(reverse=True)
ans = 0
cnt = 0
summ = sum(L)
for i in L:
    ans += i
    summ -= i
    cnt += 1
    if ans > summ:
        # print(ans, summ)
        break
print(cnt)