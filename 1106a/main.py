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
L = []
for _ in range(a):
    L.append(list(I()))
ans = 0
for i in range(1, a - 1):
    for j in range(1, a - 1):
        if L[i][j] == 'X':
            if L[i-1][j-1] == 'X' and L[i+1][j-1] == 'X' and L[i+1][j+1] == 'X' and L[i-1][j+1] == 'X':
                ans += 1
print(ans)