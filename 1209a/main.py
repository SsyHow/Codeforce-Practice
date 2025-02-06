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
L = LII()
K = [0] * 101
for i in L:
    K[i] = 1
ans = 0
for i in range(1, 101):
    if K[i] == 1:
        ans += 1
        m = i
        while m <= 100:
            K[m] = 0
            m += i
print(ans)