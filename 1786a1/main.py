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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    k = II()
    a = 1
    b = 0
    if k == 1:
        print(1, 0)
        continue
    k -= 1

    tmp = 0
    flag = True
    for i in range(2, 1500):
        if flag:
            b += min(i, k)
        else:
            a += min(i, k)
        tmp += 1
        if tmp == 2:
            tmp = 0
            flag = not flag

        k -= i
        if k <= 0:
            break
    print(a, b)