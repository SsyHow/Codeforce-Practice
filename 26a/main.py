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
b = [0] * -~a
for i in range(2, a):
    # print(b)
    for j in range(i, (b[i] < 1) * -~a, i):
        b[j] += 1
print(b.count(2))