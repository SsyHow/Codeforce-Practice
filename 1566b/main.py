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
    s = I().split('1')

    ans = 0

    for i in s:
        if i != '':
            ans += 1
        if ans == 2:
            print(2)
            break
    else:
        print(ans)
    # print(s)