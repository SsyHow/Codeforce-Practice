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
def check(n):
    if n[0] == '0':
        return False
    return True
for _ in range(a):
    s = I()
    for i in range(1, len(s)//2 + 1):
        if check(s[:i]) and check(s[i:]) and int(s[:i]) < int(s[i:]):

            print(s[:i], s[i:])
            break
    else:
        print(-1)