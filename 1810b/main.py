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
    if b & 1 == 0:
        print(-1)
        continue
    ans = []
    while b > 1:
        if b % 4 == 1:
            b = (b + 1) // 2
            ans.append(1)
        elif b % 4 == 3:
            b = (b - 1) // 2
            ans.append(2)
    print(len(ans))
    print(*ans[::-1])