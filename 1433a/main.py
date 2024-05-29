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
dic = {1:1, 2:3, 3:6, 4:10}
for i in range(a):
    b = I()

    print(int(b)%10 * 10 + dic[len(b)] - 10)