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

if a == 0:
    print(0)
else:
    cnt = i =  0
    for i in range(len(L)):
        cnt += L[i]
        if cnt >= a:
            print(i+1)
            break
    else:
        print(-1)