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

a, b = MII()
ans = 0
for _ in range(a):
    L = LII()
    for i in range(0, b*2, 2):
        # print(L[i], L[i+1])
        if L[i] == 1 or L[i+1] == 1:
            ans += 1
print(ans)