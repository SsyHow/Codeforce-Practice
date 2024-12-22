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
    c = int(b ** 0.5)
    ans = 0

    for i in range(1, c + 2):
        if b % i != 0:
            print(ans)
            break
        ans += 1
    else:
        print(ans)


