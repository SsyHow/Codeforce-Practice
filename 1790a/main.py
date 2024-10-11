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
pi = "3141592653589793238462643383279"
for _ in range(a):
    b = I()
    cnt = 0
    for i in range(len(b)):
        if pi[i] != b[i]:
            print(cnt)
            break
        cnt += 1
    else:
        print(cnt)
