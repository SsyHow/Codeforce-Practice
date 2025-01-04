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
    s = I()
    i = b - 1
    while i >= 0 and s[i] == ')':
        i -= 1
    # print(i + 1, b - i -1)
    print("YES" if b - i -1 > i + 1 else "NO")