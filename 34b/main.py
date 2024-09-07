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

def main():
    a,b = MII()
    L = LII()
    L.sort()
    ans, cnt = 0, 0
    for i in range(a):
        if cnt >= b:
            break
        if L[i] < 0:
            ans -= L[i]
        cnt += 1
    print(ans)
main()
