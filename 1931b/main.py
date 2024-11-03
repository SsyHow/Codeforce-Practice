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
    c = LII()
    avg = sum(c) // b

    cnt = 0
    for i in c:
        if i >= avg:
            cnt += i - avg
        else:
            cnt -= avg - i
        if cnt < 0:
            print("NO")
            break
    else:
        print("YES")