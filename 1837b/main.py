
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
    ans = 0
    i = j = 0
    while j < b:
        while j < b and s[i] == s[j]:
            j += 1
        ans = max(abs(j - i), ans)
        i = j
    print(ans + 1)