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
    s = I()
    ans = 0

    ans += (ord(s[0]) - ord('a')) * 25
    ans += (ord(s[1]) - ord('a')) if s[0] < s[1] else (ord(s[1]) - ord('a')) + 1
    print(ans)