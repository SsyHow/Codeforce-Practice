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
ans = 0
for i in range(1, a - 1):
    if (L[i] > L[i-1] and L[i] > L[i+1]) or (L[i] < L[i-1] and L[i] < L[i+1]):
        ans += 1
print(ans)